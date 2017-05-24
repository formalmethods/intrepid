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
import intrepyd as ip
import ip.colors as ic
import pandas as pd
import os


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
    raise NotImplementedError
    return None


def translate_lustre(infile):
    """
    Translates a lustre file into intrepyd syntax
    """
    ctx = ip.Context()

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


def simulate(ctx, cfg, verbose):
    """
    Simulates the design using default values for inputs or by taking
    input values from an existing simulation file
    """
    sim_file = cfg["simulation.file"]
    trace = ctx.mk_trace()
    depth = cfg["simulation.depth"]
    if os.path.isfile(sim_file):
        if verbose:
            print 'Re-simulating using input values from ' + sim_file
        sim_data = pd.read_csv(sim_file)
        depth = trace.set_from_pandas_dataframe(sim_data)
    else:
        if verbose:
            print 'Simulating using default values into ' + sim_file
    simulator = ctx.mk_simulator()
    simulator.simulate(trace, depth)
    dataframe = trace.get_as_dataframe(ctx.net2name)
    dataframe.write_csv(sim_file)


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
        simulate(ctx, cfg, verbose)


if __name__ == "__main__":
    cl.init()
    try:
        main()
    except:
        print ic.good('ABORTED')
        raise
    print ic.good('OK')
