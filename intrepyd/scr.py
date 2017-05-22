"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

This module implements infrastructure to deal with SCR requirements
"""

import intrepyd as ip
import intrepyd.api
import csv
import os.path

def mk_raising_edge(ctx, edgeNet, pastEdgeNet, pastWhen):
    n1 = ctx.mk_not(pastEdgeNet)
    n2 = ctx.mk_and(n1, pastWhen)
    n3 = ctx.mk_and(n2, edgeNet)
    return n3

def mk_falling_edge(ctx, edgeNet, pastEdgeNet, pastWhen):
    n1 = ctx.mk_not(edgeNet)
    n2 = ctx.mk_and(n1, pastWhen)
    n3 = ctx.mk_and(n2, pastEdgeNet)
    return n3

def mk_row_condition(ctx, inputs, pastInputs, modeStr2mode, modes, pastMode, row, rowNumber):
    assert len(inputs) == len(pastInputs)
    assert len(row) == len(inputs) + 2

    oldModeIdx = modeStr2mode[row[0]]

    if oldModeIdx == None:
        raise Exception('Cannot find mode:', row[0])

    oldModeNet = modes[oldModeIdx]

    raisingEdge = False
    fallingEdge = False
    edgeNet = None
    pastEdgeNet = None
    pastWhen = ctx.mk_eq(oldModeNet, pastMode) 

    for i in range(1, len(row) - 1):
        conj = None
        if row[i] == 't':
            conj = pastInputs[i-1]
        elif row[i] == 'f':
            conj = ctx.mk_not(pastInputs[i-1])
        elif row[i] == 'T':
            raisingEdge = True
            edgeNet = inputs[i-1]
            pastEdgeNet = pastInputs[i-1]
        elif row[i] == 'F':
            fallingEdge = True
            edgeNet = inputs[i-1]
            pastEdgeNet = pastInputs[i-1]
        else:
            pass
        if conj != None:
            pastWhen = ctx.mk_and(pastWhen, conj)

    if edgeNet == None or pastEdgeNet == None:
        raise Exception('Cannot find raising or falling edge in row ' + str(rowNumber))

    if raisingEdge:
        return mk_raising_edge(ctx, edgeNet, pastEdgeNet, pastWhen)

    if fallingEdge:
        return mk_falling_edge(ctx, edgeNet, pastEdgeNet, pastWhen)

    raise Exception('Unreachable location (is apparently reachable)')

def retrieve_modes_order(ordfilename):
    modeStr2mode = {}
    modeStr2modeValue = {}
    lines = []
    with open(ordfilename, 'r') as ordfile:
        lines = ordfile.readlines()
    i = 0
    for line in lines:
        pair = line.split()
        if len(pair) != 2:
            raise Exception('Parse error at line ' + str(i+1) + ' of ' + ordfilename)
        modeStr2mode[pair[0]] = i
        modeStr2modeValue[pair[0]] = pair[1]
        i += 1
    return modeStr2mode, modeStr2modeValue

def mk_scr_helper(ctx, csvfilename, modeStr2mode, modeStr2modeValue, inputs, pastInputs, modes, pastMode):
    firstRow = True
    result = pastMode
    rowNumber = 1
    with open(csvfilename, 'r') as csvfile:
        for row in csv.reader(csvfile, delimiter=','):
            if len(inputs) + 2 != len(row):
                raise Exception('Input number mismatch: expected ' + str(len(inputs)) + ', actual ' + str(len(row) - 2))
            if firstRow:
                firstRow = False
                continue
            rowNumber += 1
            rowCondition = mk_row_condition(ctx, inputs, pastInputs, modeStr2mode, modes, pastMode, row, rowNumber)
            rowCurrentModeStr = str(modeStr2modeValue[row[-1]])
            rowCurrentModeNet = ctx.mk_number(rowCurrentModeStr, ctx.mk_int8_type())
            if rowCurrentModeNet == None:
                raise Exception('Cannot find mode:', row[-1])
            result = ctx.mk_ite(rowCondition, rowCurrentModeNet, result)
    return result

def mk_scr(ctx, name, inputs, pastInputs, modes, pastMode):
    if len(inputs) != len(pastInputs):
        raise Exception('Inputs and past inputs differ in size')
    csvfilename = name + '.csv'
    ordfilename = name + '.ord'
    if not os.path.isfile(csvfilename):
        raise Exception('Cannot find ' + csvfilename)
    if not os.path.isfile(ordfilename):
        raise Exception('Cannot find ' + ordfilename)
    modeStr2mode, modeStr2modeValue = retrieve_modes_order(ordfilename)
    return mk_scr_helper(ctx, csvfilename, modeStr2mode, modeStr2modeValue, inputs, pastInputs, modes, pastMode)
            


