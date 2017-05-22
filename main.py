"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

Entry point
"""

import argparse as ap
import colorama as cl
import config
import pandas as pd


BAR = '#' * 64
SPLASH =\
'\n' + BAR +\
r"""

      .__        __                                  .___
      |__| _____/  |________   ____ ______ ___.__. __| _/
      |  |/    \   __\_  __ \_/ __ \\____ <   |  |/ __ |
      |  |   |  \  |  |  | \/\  ___/|  |_> >___  / /_/ |
      |__|___|  /__|  |__|    \___  >   __// ____\____ |
              \/                  \/|__|   \/         \/
      https://github.com/formalmethods/intrepyd

""" + BAR + '\n'


def parse_arguments():
    """
    Command-line parser
    """
    arg_parser = ap.ArgumentParser(prog='intrepyd',
                                   formatter_class=ap.ArgumentDefaultsHelpFormatter)
    arg_parser.add_argument('INFILE',
                            help='The input file to process')
    arg_parser.add_argument('-c', '--config', default='config.json',
                            help='Specifies a config file')
    return arg_parser.parse_args()


def translate_simulink(infile):
    """
    Translates a simulink file into intrepyd syntax
    """
    return None


def translate_lustre(infile):
    """
    Translates a lustre file into intrepyd syntax
    """
    return None


def translate_infile(infile):
    """
    Translates an input file depending on the suffix
    """
    ctx = None
    if infile[-4:] == '.slx' or infile[-4:] == '.mdl':
        ctx = translate_simulink(infile)
    elif infile[-4:] == '.lus' or infile[-4:] == '.ec':
        ctx = translate_lustre(infile)
    else:
        raise RuntimeError('Did not recognize a file extension in [slx, mdl, lus, ec]')
    return ctx


def main():
    """
    Main
    """
    parsed_args = parse_arguments()
    cfg = config.Config.get_instance(parsed_args.config)
    verbose = cfg["verbose"]
    if verbose:
        print 'Parsing input file'
    ctx = translate_infile(parsed_args.INFILE)
    if verbose:
        print SPLASH
    if cfg["simulation"]:
        if verbose:
            print 'Running simulation'
        sim_file = cfg["simulation.file"]
        sim_data = pd.read_csv(sim_file)

if __name__ == "__main__":
    cl.init()
    main()
