"""
Implementation of plotting services for traces
"""

from matplotlib import pyplot as plt
import intrepyd as ip

def _create_subplot(all_plots, num, x, y, legend):
    y = [int(elem) for elem in y]
    miny = min(y)
    maxy = max(y)
    subplot = plt.subplot(all_plots, 1, num)
    subplot.axes.set_xticks(x)
    subplot.axes.set_yticks(range(miny, maxy + 1))
    subplot.set_ylim(miny - 1, maxy + 1)
    plt.step(x, y, label=legend)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # plt.plot()

def plot_trace_dataframe(dataframe):
    """
    Draws one step plot per each signal in the trace.

    Args:
        dataframe (DataFrame): the dataframe of the trace
    """
    if dataframe is None:
        raise Exception('Null trace given as input')

    if len(dataframe.index) == 0:
        return

    # Computes the step numerals [0, ...]
    steps = range(len(dataframe.columns) + 1)

    # Preprocess the trace duplicating the first value.
    # This is a visual trick to make plots look nicer (in particular
    # to have a better displaying of the first value that would
    # otherwise be hidden by the y-axis. Also turn 'true' in 1,
    # 'false' in 0, '?' in 0
    for key in dataframe.index:
        if len(dataframe.loc[key]) == 0:
            raise Exception('Unexpected trace with no values')
        for value in range(len(dataframe.loc[key])):
            val = dataframe.loc[key][value]
            val = ip.trace.Trace.get_numeric_value(val)
            if val == '?':
                dataframe.loc[key][value] = -1
            else:
                dataframe.loc[key][value] = val
    # Adding a column at the end
    dataframe[len(dataframe.columns)] = [0 for _ in range(len(dataframe.index))]
    # Shifting all cols on the right
    for col in range(len(dataframe.columns) - 2, -1, -1):
        dataframe[col + 1] = dataframe[col]

    # Create the plots, one in each subplot
    all_plots = len(dataframe.index)
    num = 1
    for key in dataframe.index:
        _create_subplot(all_plots, num, steps, dataframe.loc[key], key)
        num += 1

    plt.tight_layout()
    plt.show()

def plot_trace_dictionary(net_dict):
    """
    Draws one step plot per each signal in the trace.

    Args:
        net_dict (Dictionary): the dictionary of the trace
    """
    if net_dict is None:
        raise Exception('Null trace given as input')
    if len(net_dict.keys()) == 0:
        return
    # Computes the step numerals [0, ...]
    steps = range(len(net_dict[list(net_dict.keys())[0]]) + 1)

    # Preprocess the trace duplicating the first value.
    # This is a visual trick to make plots look nicer (in particular
    # to have a better displaying of the first value that would
    # otherwise be hidden by the y-axis. Also turn 'true' in 1,
    # 'false' in 0, '?' in 0
    for key in net_dict.keys():
        if len(net_dict[key]) == 0:
            raise Exception('Unexpected trace with no values')
        for value in range(len(net_dict[key])):
            val = net_dict[key][value]
            val = ip.trace.Trace.get_numeric_value(val)
            if val == '?':
                net_dict[key][value] = -1
            else:
                net_dict[key][value] = val
        net_dict[key].insert(0, net_dict[key][0])

    # Create the plots, one in each subplot
    all_plots = len(net_dict.keys())
    num = 1
    for key in net_dict.keys():
        _create_subplot(all_plots, num, steps, net_dict[key], key)
        num += 1

    plt.tight_layout()
    plt.show()
