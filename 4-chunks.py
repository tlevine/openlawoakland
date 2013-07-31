#!/usr/bin/env python
import re

chapter_regex = re.compile(r'^Chapter ([0-9]+\.[0-9]+)$')
section_regex = re.compile(r'^([0-9]+\.[0-9]+\.[0-9]+)(.*)$')

volume = open('tmp/volume1.txt')
chunks = {}
section = None
while True:
    line = volume.readline()

    if line == '':
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
