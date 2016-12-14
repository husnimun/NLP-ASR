#!/usr/bin/python

from os import listdir
from os.path import isfile, join, splitext

files = []
transcripts = []
transcript_prefix = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

for prefix in transcript_prefix:
    myFiles =  [f for f in listdir('./set_2/' + prefix) if isfile(join('./set_2/' + prefix, f))]
    myFiles.sort()
    files += myFiles
    transcripts += open('transcript/' + prefix + '-raw.tsv').read().splitlines()

transcripts = [transcript.split('\t')[1].lower() for transcript in transcripts]

with open('words.mlf', 'w') as words_mlf:
    words_mlf.write('#!MLF!#\n')
    i = 0
    for f in files:
        filename, extension = splitext(f)
        words_mlf.write('"*/{0}.lab"\n'.format(filename))
        transcript = transcripts[i].replace('.', '')
        transcript = transcript.replace(',', '')
        transcript = transcript.replace('!', '')
        transcript = transcript.replace(':', '')
        transcript = transcript.replace('?', '')
        transcript = transcript.replace('\'', '')
        transcript = transcript.replace('\"', '')
        
        for t in transcript.split():
            words_mlf.write('{0}\n'.format(t))
        words_mlf.write('.\n')

        i += 1

