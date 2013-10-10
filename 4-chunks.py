#!/usr/bin/env python
import os, json
from lib import chunk

fp_out_all = open(os.path.join('tmp', 'chunks.json'))
all_chunks = []
for volume in ['volume1', 'volume2', 'planning']:
    fp_in  = open(os.path.join('tmp', volume + '.txt' ), 'r')
    fp_out = open(os.path.join('tmp', volume + '.json'), 'w')
    chunks = chunk(fp_in)
    all_chunks.extend(chunks)
    json.dump(chunks, fp_out)
json.dump(all_chunks, fp_out_all)
