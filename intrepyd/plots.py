"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

This module implements plotting services
"""

import intrepyd as ip
import intrepyd.trace
from matplotlib import pyplot as plt

def create_subplot(allPlots, n, x, y, legend):
    y = [int(elem) for elem in y]
    miny = min(y)
    maxy = max(y)
    subplot = plt.subplot(allPlots, 1, n)
    subplot.axes.set_xticks(x)
    subplot.axes.set_yticks(range(miny, maxy + 1))
    subplot.set_ylim(miny - 1, maxy + 1)
    plt.step(x, y, label=legend)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # plt.plot()

def plot_trace_dictionary(trace):
    """
    Draws one step plot per each signal in the trace.

    Args:
        trace (Dictionary): the dictionary of the trace
    """
    if trace == None:
        raise Exception('Null trace given as input')

    if len(trace.keys()) == 0:
        return

    # Computes the step numerals [0, ...]
    steps = [step for step in range(len(trace[trace.keys()[0]]) + 1)]

    # Preprocess the counterexample duplicate the first value.
    # This is a visual trick to make plots look nicer (in particular
    # to have a better displaying of the first value that would
    # otherwise be hidden by the y-axis. Also turn 'true' in 1,
    # 'false' in 0, '?' in 0
    for key in trace.keys():
        if len(trace[key]) == 0:
            raise Exception('Unexpected trace with no values')
        for value in range(len(trace[key])):
            v = trace[key][value]
            v = ip.trace.Trace.get_numeric_value(v)
            if v == '?':
                trace[key][value] = 0
            else:
                trace[key][value] = v
        trace[key].insert(0, trace[key][0])

    # Create the plots, one in each subplot
    allPlots = len(trace.keys())
    n = 1
    for key in trace.keys():
       create_subplot(allPlots, n, steps, trace[key], key) 
       n += 1

    plt.tight_layout()
    plt.show()
