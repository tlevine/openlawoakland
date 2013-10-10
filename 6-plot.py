#!/usr/bin/env python
import os
import json

import matplotlib.pyplot as plt
import networkx as nx

g = nx.read_adjlist(os.path.join('tmp', 'cross-references.adjlist'), delimiter = ',')
# colors=range(20)
# pos=nx.spring_layout(g)
# nx.draw(g,pos,node_color='#A0CBE2',edge_color=colors,width=4,edge_cmap=plt.cm.Blues,with_labels=False)

g_9_56_090 = nx.ego_graph(g, '9.56.090')
nx.draw_spring(g_9_56_090)
plt.savefig("9.56.090.png")
