#!/usr/bin/env python
import os
import json

import matplotlib.pyplot as plt
import networkx as nx


g = nx.read_adjlist(os.path.join('tmp', 'cross-references.adjlist'), delimiter = ',')
nodes = json.load(open(os.path.join('tmp', 'chunks.json')))

def ego():
    '''
    This node is deceptively connected because it's from the index
    (page 750 of volume2.pdf).
    '''
    g_9_56_090 = nx.ego_graph(g, '9.56.090')
    nx.draw_spring(g_9_56_090)
    plt.savefig("9.56.090.png")
    print nodes['9.56.090'
