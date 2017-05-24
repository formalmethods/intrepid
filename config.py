"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 22/05/2017

Retrieve values from the configuration file
"""
import json

class Config(object):
    """
    Stores configuration options
    """
    instance = None

    @staticmethod
    def get_instance(filename=None):
        """
        Implementation of Singleton pattern
        """
        if Config.instance is None:
            assert not filename is None
            Config.instance = Config(filename)
        return Config.instance.config

    def __init__(self, filename):
        with open(filename) as fdesc:
            config_string = ''
            for line in fdesc.readlines():
                line = line.lstrip()
                if len(line) > 2 and line[0] == '/' and line[1] == '/':
                    # Ignores commented-out lines
                    continue
                config_string += line
            self._config = json.loads(config_string)

    @property
    def config(self):
        """
        Getter
        """
        return self._config
