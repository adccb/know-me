#!/usr/bin/env python3

from argparse import ArgumentParser

from lib.plotter import generate_graph

blocks = {
    'p': [ 'paranoia', 'fragility', 'energy', 'hallucination', 'fear' ],
    'd': [ 'dp', 'dissociation', 'fragility', 'ideation' ]
}

def render_graphs(args):
    graphs = []

    # premade blocks
    if args.b:
        return generate_graph(blocks[args.b])

    # a la carte
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

    generate_graph(graphs)

if __name__ == '__main__':
    parser = ArgumentParser(description='build a graph')
    parser.add_argument('-b',  metavar='B', help='block mode; select a block')
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
    graphs = parser.parse_args()
    render_graphs(graphs)

