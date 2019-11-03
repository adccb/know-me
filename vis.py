#!/usr/bin/env python3

from argparse import ArgumentParser
from datetime import datetime
import csv
from random import shuffle

import matplotlib
import matplotlib.pyplot as plt

data = {}
with open('./data.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader) # skip the headers
    for row in reader:
        epoch, _, _, tracker, value, *rest = row
        if not tracker in data:
            data[tracker] = []
        data[tracker].append((int(epoch) / 1000, float(value)))

formats = ['bo-', 'go-', 'ro-', 'co-', 'mo-', 'yo-', 'ko-']
bar_charts = [
    'hallucination',
    'memory_lost'
]

def plot_line(ax, key, fmt):
    row = data[key]
    values = [ __transform_data(key, value) for epoch, value in row ]
    list_of_datetimes = [ datetime.fromtimestamp(epoch) for epoch, value in row ]
    dates = matplotlib.dates.date2num(list_of_datetimes)
    ax.plot_date(dates, values, fmt, label=key)

def plot_bar_chart(ax, key, fmt):
    try:
        row = data[key]
    except KeyError:
        return False

    dates = [ datetime.fromtimestamp(epoch) for epoch, value in row ]
    values = [ value for epoch, value in row ]
    plt.bar(dates, values, 0.005, label=key, color=fmt[0])

def generate_graph(*graphs):
    fig, ax = plt.subplots()
    ax.grid(True)
    plt.gcf().autofmt_xdate()
    shuffle(formats)
    for idx, graph_name in enumerate(graphs):
        if graph_name in bar_charts:
            plot_bar_chart(ax, graph_name, formats[idx])
        else:
            plot_line(ax, graph_name, formats[idx])

    ax.legend()
    plt.show()

def __transform_data(key, data):
    if key == 'fear' or key == 'sleep_quality':
        return data / 20
    if key == 'ideation':
        return data / 10
    else:
        return data

if __name__ == '__main__':
    parser = ArgumentParser(description='build a graph')
    parser.add_argument('-d', action='store_true', default=False, help='add dp/dr')
    parser.add_argument('-e', action='store_true', default=False, help='add energy')
    parser.add_argument('-f', action='store_true', default=False, help='add fragility')
    parser.add_argument('-i', action='store_true', default=False, help='add ideation')
    parser.add_argument('-l', action='store_true', default=False, help='add hallucinations')
    parser.add_argument('-m', action='store_true', default=False, help='add mood')
    parser.add_argument('-p', action='store_true', default=False, help='add paranoia')
    parser.add_argument('-r', action='store_true', default=False, help='add rq')
    parser.add_argument('-s', action='store_true', default=False, help='add fear')
    parser.add_argument('-y', action='store_true', default=False, help='add memory lost')
    args = parser.parse_args()

    graphs = []

    if args.d:
        graphs = graphs + ['dp', 'dissociation']
    args.e and graphs.append('energy')
    args.f and graphs.append('fragility')
    args.i and graphs.append('ideation')
    args.l and graphs.append('hallucination')
    args.m and graphs.append('mood')
    args.p and graphs.append('paranoia')
    args.r and graphs.append('sleep_quality')
    args.s and graphs.append('fear')
    args.y and graphs.append('memory_lost')

    generate_graph(*graphs)

