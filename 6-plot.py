#!/usr/bin/env python
import os

import networkx

g = networkx.read_adjlist(os.path.join('tmp', 'cross-references.adjlist'), delimiter = ',')
