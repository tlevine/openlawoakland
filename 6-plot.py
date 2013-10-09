#!/usr/bin/env python
import os

import matplotlib.pyplot as plt
import networkx as nx

g = nx.read_adjlist(os.path.join('tmp', 'cross-references.adjlist'), delimiter = ',')
# colors=range(20)
# pos=nx.spring_layout(g)
# nx.draw(g,pos,node_color='#A0CBE2',edge_color=colors,width=4,edge_cmap=plt.cm.Blues,with_labels=False)
nx.draw_circular(g)
plt.savefig("edge_colormap.png") # save as png
plt.show() # display
