#!/usr/bin/env python
import os, json
from lib import chunk

for volume in ['volume1', 'volume2', 'planning']:
    fp_in  = open(os.path.join('tmp', volume + '.txt' ), 'r')
    fp_out = open(os.path.join('tmp', volume + '.json'), 'w')
    chunks = chunk(fp_in)
    json.dump(chunks, fp_out)
