"""
Copyright (C) 2019 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/02/2019

Utility function for the translator
"""

def sanitizeName(name):
    return name.replace('.', '_')