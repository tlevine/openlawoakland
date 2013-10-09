#!/usr/bin/env python
import os, json, csv
import lib

for volume in ['volume1', 'volume2', 'planning']:
    fp_in  = open(os.path.join('tmp', volume + '.json' ), 'r')
    fp_out = open(os.path.join('tmp', volume + '.csv'), 'w')
    csv_out = csv.writer(fp_out)
    chunks = json.load(fp_in)
    result = lib.network(chunks)
    csv_out.writerow(('from','to'))
    for adjacency in result:
        csv_out.writerow(adjacency)
    fp_in.close()
    fp_out.close()
