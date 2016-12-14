#!/usr/bin/python

import string

lines = []
wlist = []
transcript_prefix = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

for prefix in transcript_prefix:
    lines += open('transcript/' + prefix + '-raw.tsv').read().splitlines()

lines = [line.lower() for line in lines]

for line in lines: 
    line_new = line.translate(None, string.punctuation)
    transcript = line_new.split()[1]
    wlist += [w for w in transcript.split() if w not in wlist]

wlist.sort()

with open('wlist.txt', 'w') as wlist_file:
    for w in wlist:
        wlist_file.write('{0}\n'.format(w))