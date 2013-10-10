#!/usr/bin/env python
import re

chapter_regex = re.compile(r'^Chapter ([0-9]+\.[0-9]+)$')
section_regex = re.compile(r'^([0-9]+\.[0-9]+\.[0-9]+)(.*)$')
citation_regex = re.compile(r'([0-9]+\.[0-9]+\.[0-9]+)')

'''
Deal with the index and tables!
Stop at this phrase:

STATUTORY REFERENCES
FOR
CALIFORNIA CITIES

Also, maybe avoid overwriting the node.
'''

def chunk(fp):
    '''
    >>> chunk(open('tmp/volume1.txt'))
    '''
    chunks = {}
    section = None
    while True:
        line = fp.readline()

        if line in {'', 'CALIFORNIA CITIES'}:
            # Stop at the end of the file.
            break

        m = re.match(chapter_regex, line)
        if m:
            # Create a new chapter
            section = m.group(1)
            chunks[section] = m.group(1) + '\n'
            continue

        m = re.match(section_regex, line)
        if m:
            # Create a new section
            section = m.group(1)
            chunks[section] = m.group(2) + '\n'
        elif section:
            # Add to the section
            chunks[section] += line
        else:
            # The first section has yet to start.
            pass
    return chunks

def network(chunks):
    '''
    >>> list(network({'8.03.050': 'Also see OMC Section 5.34.051.)', '5.34.051': 'pursuant to Section 5.34.080.'}))
    [('8.03.050','5.34.051'),('5.34.051','5.34.080')]
    '''
    for k,v in chunks.items():
        for crossreference in re.findall(citation_regex, v):
            yield k, crossreference
