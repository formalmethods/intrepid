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
import os
import multiprocessing as mp
import time
import importlib
import subprocess as sp
import pandas as pd
import colorama as cl
import intrepyd.colors as ic
import intrepyd.lustre2py.translator as tr
import intrepyd.engine as en
import intrepyd.config as cg
import intrepyd.tools as ts
import intrepyd


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


def translate_infile(infile, cfg):
    """
    Translates an input file depending on the suffix
    """
    enc = None
    if infile[-4:] == '.slx' or infile[-4:] == '.mdl':
        enc = ts.translate_simulink(infile, cfg['simulink.type.real'])
    elif infile[-4:] == '.lus' or infile[-4:] == '.ec':
        enc = ts.translate_lustre(infile, cfg['lustre.topnode'], cfg['lustre.type.real'])
    else:
        raise RuntimeError('Did not recognize a file extension in [slx, mdl, lus, ec]')
    return enc


def main():
    """
    Main
    """
    parsed_args = parse_arguments()
    infile = parsed_args.INFILE
    cfg = cg.Config.get_instance(parsed_args.config)
    enc = translate_infile(infile, cfg)
    ctx = intrepyd.Context()
    circ = enc.mk_instance(ctx, infile)
    circ.mk_circuit()
    print circ.outputs


if __name__ == "__main__":
    cl.init()
    try:
        main()
    except:
        print ic.fail('ABORTED')
        raise
