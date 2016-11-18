import intrepid as ip
import intrepid.exceptions as ipex
import csv
import os.path

def mk_raising_edge(ctx, edgeNet, pastEdgeNet, pastWhen):
    n1 = ip.mk_not(ctx, pastEdgeNet)
    n2 = ip.mk_and(ctx, n1, pastWhen)
    n3 = ip.mk_and(ctx, n2, edgeNet)
    return n3

def mk_falling_edge(ctx, edgeNet, pastEdgeNet, pastWhen):
    n1 = ip.mk_not(ctx, edgeNet)
    n2 = ip.mk_and(ctx, n1, pastWhen)
    n3 = ip.mk_and(ctx, n2, pastEdgeNet)
    return n3

def mk_row_condition(ctx, inputs, pastInputs, modeStr2mode, modes, pastMode, row):
    assert len(inputs) == len(pastInputs)
    assert len(row) == len(inputs) + 2

    oldModeIdx = modeStr2mode[row[0]]

    if oldModeIdx == None:
        raise ipex.IntrepidException('Cannot find mode:', row[0])

    oldModeNet = modes[oldModeIdx]

    raisingEdge = False
    fallingEdge = False
    edgeNet = None
    pastEdgeNet = None
    pastWhen = ip.mk_eq(ctx, oldModeNet, pastMode) 
    for i in range(1, len(row) - 1):
        conj = None
        if row[i] == 't':
            conj = pastInputs[i-1]
        elif row[i] == 'f':
            conj = ip.mk_not(ctx, pastInputs[i-1])
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
            pastWhen = ip.mk_and(ctx, pastWhen, conj)

    if edgeNet == None or pastEdgeNet == None:
        raise ipex.IntrepidException('Cannot find raising or falling edge in row')

    if raisingEdge:
        return mk_raising_edge(ctx, edgeNet, pastEdgeNet, pastWhen)

    if fallingEdge:
        return mk_falling_edge(ctx, edgeNet, pastEdgeNet, pastWhen)

    assert false
    return None

def retrieve_modes_order(ordfilename):
    modeStr2mode = {}
    modes = []
    with open(ordfilename, 'r') as ordfile:
        modes = ordfile.readlines()
    i = 0
    for mode in modes:
        modeStr2mode[mode.rstrip()] = i
        i += 1
    return modeStr2mode

def mk_scr_helper(ctx, csvfilename, modeStr2mode, inputs, pastInputs, modes, pastMode):
    firstRow = True
    result = pastMode
    with open(csvfilename, 'r') as csvfile:
        for row in csv.reader(csvfile, delimiter=','):
            if len(inputs) + 2 != len(row):
                raise ipex.IntrepidException('Input number mismatch')
            if firstRow:
                firstRow = False
                continue
            rowCondition = mk_row_condition(ctx, inputs, pastInputs, modeStr2mode, modes, pastMode, row)
            rowCurrentModeStr = str(modeStr2mode[row[-1]])
            rowCurrentMode = ip.mk_number(ctx, rowCurrentModeStr, ip.mk_int8_type(ctx))
            if rowCurrentMode == None:
                raise ipex.IntrepidException('Cannot find mode:', row[-1])
            rowCondition = ip.mk_true(ctx)
            result = ip.mk_ite(ctx, rowCondition, rowCurrentMode, result)
    return result

def mk_scr(ctx, name, inputs, pastInputs, modes, pastMode):

    if len(inputs) != len(pastInputs):
        raise ipex.IntrepidException('Inputs and past inputs differ in size')

    csvfilename = name + '.csv'
    ordfilename = name + '.ord'

    if not os.path.isfile(csvfilename):
        raise ipex.IntrepidException('Cannot find ' + csvfilename)

    if not os.path.isfile(ordfilename):
        raise ipex.IntrepidException('Cannot find ' + ordfilename)

    modeStr2mode = retrieve_modes_order(ordfilename)
    return mk_scr_helper(ctx, csvfilename, modeStr2mode, inputs, pastInputs, modes, pastMode)
            


