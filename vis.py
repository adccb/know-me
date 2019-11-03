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

def plot_line(ax, key, fmt):
    row = data[key]
    values = [ value for epoch, value in row ]
    list_of_datetimes = [ datetime.fromtimestamp(epoch) for epoch, value in row ]
    dates = matplotlib.dates.date2num(list_of_datetimes)
    ax.plot_date(dates, values, fmt, label=key)

def generate_graph(*graphs):
    fig, ax = plt.subplots()
    ax.grid(True)
    plt.gcf().autofmt_xdate()
    shuffle(formats)
    for idx, graph_name in enumerate(graphs):
        plot_line(ax, graph_name, formats[idx])
    ax.legend()
    plt.show()

if __name__ == '__main__':
    parser = ArgumentParser(description='build a graph')
    parser.add_argument('-m', action='store_true', default=False, help='add mood')
    parser.add_argument('-e', action='store_true', default=False, help='add energy')
    parser.add_argument('-f', action='store_true', default=False, help='add fragility')
    parser.add_argument('-p', action='store_true', default=False, help='add paranoia')
    parser.add_argument('-d', action='store_true', default=False, help='add dp/dr')
    args = parser.parse_args()

    graphs = []
    args.m and graphs.append('mood')
    args.e and graphs.append('energy')
    args.f and graphs.append('fragility')
    args.p and graphs.append('paranoia')
    if args.d:
        graphs = graphs + ['dp', 'dissociation']
    
    generate_graph(*graphs)

