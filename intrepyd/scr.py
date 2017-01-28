import intrepyd as ip
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
        raise Exception('Cannot find raising or falling edge in row ' + str(rowNumber))

    if raisingEdge:
        return mk_raising_edge(ctx, edgeNet, pastEdgeNet, pastWhen)

    if fallingEdge:
        return mk_falling_edge(ctx, edgeNet, pastEdgeNet, pastWhen)

    assert false
    return None

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
            rowCurrentModeNet = ip.mk_number(ctx, rowCurrentModeStr, ip.mk_int8_type(ctx))
            if rowCurrentModeNet == None:
                raise Exception('Cannot find mode:', row[-1])
            result = ip.mk_ite(ctx, rowCondition, rowCurrentModeNet, result)
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
            


