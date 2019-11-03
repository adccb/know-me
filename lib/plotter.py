from datetime import datetime
from random import shuffle

import matplotlib
import matplotlib.pyplot as plt

from lib.normalize_data import normalize_data 
from lib.fetcher import data, get_row
from lib.formats import fmt

bar_charts = [ 'hallucination', 'memory_lost' ]

def plot_line(ax, key, fmt):
    row = get_row(key)
    values = [ normalize_data(key, value) for epoch, value in row ]
    list_of_datetimes = [ datetime.fromtimestamp(epoch) for epoch, value in row ]
    dates = matplotlib.dates.date2num(list_of_datetimes)
    ax.plot_date(dates, values, fmt, label=key)

def plot_bar_chart(ax, key, fmt):
    row = get_row(key)
    dates = [ datetime.fromtimestamp(epoch) for epoch, value in row ]
    values = [ value for epoch, value in row ]
    plt.bar(dates, values, 0.005, label=key, color=fmt[0])

def generate_graph(graphs):
    fig, ax = plt.subplots()

    # plot the actual data
    for idx, graph_name in enumerate(graphs):
        if graph_name in bar_charts:
            plot_bar_chart(ax, graph_name, fmt(idx))
        else:
            plot_line(ax, graph_name, fmt(idx))

    # "computer, make the graph look pretty"
    ax.grid(True)
    ax.set_xlabel('time')
    ax.set_ylabel('score')
    ax.set_title("%s / time" % (', '.join(graphs)))
    ax.legend()
    plt.gcf().autofmt_xdate()
    plt.show()

