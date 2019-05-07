#!/usr/bin/python

import sys
import json


class Id(object):

    def __init__(self):
        super().__init__()
        self._i = 0

    @property
    def i(self):
        self._i += 1
        return self._i


def main(args):
    _parse_args(args)
    print("""
digraph G {
    graph [rankdir=LR]
    node [shape=box,
    style=solid
    ]
    edge [color="#00000088",
    dir=back
    ]
    """)
    i = Id()
    for graph in json.load(sys.stdin):
        print_single_graph(graph, i)
    print("}")


def print_single_graph(graph, i):
    name_to_node = {}
    print("subgraph cluster{}{{".format(i.i))
    
    parents = []
    for target, deps in graph.items():
        target_str = _escape(target)
        parents.append(target_str)
    
    for target, deps in graph.items():
        target_str = _escape(target)
        _register_node(target_str, i, name_to_node)
        target_node = name_to_node[target_str]
        for dep_str in (_escape(dep) for dep in deps):
            if dep_str in parents:
                _register_node(dep_str, i, name_to_node)
            else:
                _register_filled_node(dep_str, i, name_to_node)
            print('{} -> {}'.format(target_node, name_to_node[dep_str]))
    print("}")

def _register_node(name, i, name_to_node):
    if not (name in name_to_node):
        node = 'n{}'.format(i.i)
        name_to_node[name] = node
        print('{}[label={}]'.format(node, name))
        
def _register_filled_node(name, i, name_to_node):
    if not (name in name_to_node):
        node = 'n{}'.format(i.i)
        name_to_node[name] = node
        print('{}[label={}, style = "solid,filled"]'.format(node, name))

def _escape(s):
    return '"{}"'.format(s.replace('"', r'\"'))


def _parse_args(args):
    if len(args) != 1:
        print('# convert a dependency graph stored in JSON format to DOT format')
        print('{} < deps.json | dot -Tpdf >| workflow.pdf'.format(args[0]))
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
