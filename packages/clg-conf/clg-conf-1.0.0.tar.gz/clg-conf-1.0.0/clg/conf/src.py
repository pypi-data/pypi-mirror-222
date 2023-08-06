# coding: utf-8

import os
import sys
import clg
import yaml
import yamlloader
from addict import Dict
from collections import OrderedDict

DEFAULT_CONF_FILE = os.path.join(sys.path[0], 'conf.yml')
DEFAULT_CONF_DIR = os.path.join(sys.path[0], 'conf')

class CLGConfigError(Exception):
    pass

def replace_paths(value):
    """Replace *__FILE__* string in ``value`` (if it is not a string, recursively
    parse the data) by the path of the main script (``sys.path[0]``).
    """
    return {
        str: lambda: value.replace('__FILE__', sys.path[0]),
        list: lambda: [replace_paths(elt) for elt in value],
        dict: lambda: {key: replace_paths(val) for key, val in value.items()},
        OrderedDict: (lambda:
            OrderedDict((key, replace_paths(val)) for key, val in value.items()))
    }.get(type(value), lambda: value)()


class Config(OrderedDict):
    def init(self, args, **kwargs):
        """Initialize the object with command-line arguments ``args``."""
        # Retrieve configuration file and directory or set defaults.
        conf_file = os.path.expanduser(
            args._get('conf_file', kwargs.pop('conf_file', DEFAULT_CONF_FILE)))
        conf_dir = os.path.expanduser(
            args._get('conf_dir', kwargs.pop('conf_dir', DEFAULT_CONF_DIR)))
        commands = [value for (arg, value) in sorted(args) if arg.startswith('command')]

        # Load main configuration file.
        if os.path.exists(conf_file):
            self.load_cmd_file(conf_file)

        # Load intermediary configuration files.
        if os.path.isdir(conf_dir):
            self.load_dir(conf_dir, clg.config, commands)

    def __getattribute__(self, name):
        """Allow direct access to elements in uppercase."""
        if name.isupper():
            try:
                return self[name]
            except KeyError as err:
                raise CLGConfigError("key '{:s}' not found in configuration"
                                     .format(err.args[0]))
        else:
            return OrderedDict.__getattribute__(self, name)

    def __setattr__(self, name, value):
        """Allow elements in uppercase to be added to the OrderedDict."""
        if name.isupper():
            self[name] = value
        else:
            return OrderedDict.__setattr__(self, name, value)

    def load_cmd_file(self, filepath):
        """Load YAML file ``filepath`` and add each element to the object.."""
        try:
            conf = yaml.load(open(filepath), Loader=yamlloader.ordereddict.CLoader)
        except (IOError, yaml.YAMLError) as err:
            raise CLGConfigError('(%s) unable to load file: %s' % (filepath, err))

        for param, value in conf.items():
            setattr(self, param.upper(), replace_paths(value))

    def load_dir(self, dirpath, config, commands):
        """Recursively load ``dirpath`` directory for adding elements in the object
        based on the current configuration ``config`` and the current ``commands``.
        """
        def get_subcommands(config):
            return ({}
                    if not 'subparsers' in config
                    else config['subparsers'].get('parsers', config['subparsers']))

        config = get_subcommands(config)

        while commands:
            cur_command = commands.pop(0)

            # Load command's configuration file and directory.
            cmd_dirpath = os.path.join(dirpath, cur_command)
            cmd_filepath = '%s.yml' % cmd_dirpath
            if os.path.exists(cmd_filepath):
                self.load_cmd_file(cmd_filepath)
            if os.path.exists(cmd_dirpath):
                # Be sure directory is loaded for last commands (tree's leaves).
                self.load_dir(cmd_dirpath, config[cur_command], commands or [cur_command])

            # Load files and directories that are not for other subcommands.
            for filename in sorted(os.listdir(dirpath)):
                # Ignore hidden files.
                if filename.startswith('.'):
                    continue

                filepath = os.path.join(dirpath, filename)
                if os.path.isfile(filepath):
                    filename, fileext = os.path.splitext(filename)
                    if filename not in config:
                        setattr(self, filename.upper(), self.load_file(filepath))
                elif filename not in config:
                    setattr(self, filename.upper(), self.load_subdir(filepath))

    def load_subdir(self, dirpath):
        """Recursively parse ``dirpath`` directory for retrieving all
        configuration elements.
        """
        conf = Dict()
        for filename in sorted(os.listdir(dirpath)):
            filepath = os.path.join(dirpath, filename)
            if os.path.isfile(filepath):
                conf[os.path.splitext(filename)[0]] = self.load_file(filepath)
            else:
                conf[filename] = self.load_subdir(filepath)
        return conf

    def load_file(self, filepath):
        """Load ``filepath`` file based on its extension."""
        _, fileext = os.path.splitext(filepath)
        with open(filepath) as fhandler:
            return replace_paths({
                '.yml': lambda: yaml.load(fhandler, Loader=yamlloader.ordereddict.CLoader),
                '.json': lambda: json.load(fhandler, object_pairs_hook=OrderedDict)
            }.get(fileext, lambda: fhandler.read())())

    def pprint(self):
        """Pretty print the object using `json` module."""
        import json
        return json.dumps(OrderedDict(self.items()), indent=4)
