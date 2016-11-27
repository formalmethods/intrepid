import intrepid as ip
from matplotlib import pyplot as plt

def create_subplot(allPlots, n, x, y, legend):
    subplot = plt.subplot(allPlots, 1, n)
    subplot.axes.set_xticks(n)
    subplot.axes.set_yticks([0, 1])
    subplot.set_ylim(-1, 2)
    plt.step(x, y)
    plt.legend(legend)

def plot_counterexample_dictionary(cex):
    """
    Draws one step plot per each signal in the counterexample.

    Parameters
    ----------
    cex: the dictionary of the counterexample
    """

    if len(cex.keys()) == 0:
        return

    # Computes the step numerals [0, ...]
    steps = [step for step in range(len(cex[cex.keys()[0]]) + 1)]

    # Preprocess the counterexample duplicate the first value.
    # This is a visual trick to make plots look nicer (in particular
    # to have a better displaying of the first value that would
    # otherwise be hidden by the y-axis. Also turn 'true' in 1,
    # 'false' in 0, '?' in 0
    for key in cex.keys():
        if len(cex[key]) == 0:
            ip.exceptions.IntrepidException('Unexpected counterexample with no values')
        for value in len(cex[key]):
            v = cex[key][value]
            if v == 'true':
                cex[key][value] = 1
            elif v == 'false' or v == '?':
                cex[key][value] = 0
        cex[key].insert(0, cex[key][0])

    # Create the plots, one in each subplot
    allPlots = len(cex.keys())
    n = 1
    for key in cex.keys():
       create_subplot(allPlots, n, steps, cex[key], key) 

    plt.show()
