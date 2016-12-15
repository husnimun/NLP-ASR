#!/usr/bin/python

#!/usr/bin/python

from os import listdir
from os.path import isfile, join, splitext

files = []
transcripts = {}

files = [f for f in listdir('./wav') if isfile(join('./wav', f))]
files.sort()

transcripts['A'] = open('transcript/A-raw.tsv').read().splitlines()
transcripts['B'] = open('transcript/B-raw.tsv').read().splitlines()
transcripts['C'] = open('transcript/C-raw.tsv').read().splitlines()
transcripts['D'] = open('transcript/D-raw.tsv').read().splitlines()
transcripts['E'] = open('transcript/E-raw.tsv').read().splitlines()
transcripts['F'] = open('transcript/F-raw.tsv').read().splitlines()
transcripts['G'] = open('transcript/G-raw.tsv').read().splitlines()
transcripts['H'] = open('transcript/H-raw.tsv').read().splitlines()
transcripts['I'] = open('transcript/I-raw.tsv').read().splitlines()
transcripts['J'] = open('transcript/J-raw.tsv').read().splitlines()

with open('words.mlf', 'w') as words_mlf:
	words_mlf.write('#!MLF!#\n')
	for f in files:
		filename, extension = splitext(f)
		words_mlf.write('"*/{0}.lab"\n'.format(filename))
		transcript_code = filename[-4:]
		transcript_prefix = transcript_code[0]
		transcript_num = int(transcript_code[1:]) - 1

		transcript_line = transcripts[transcript_prefix][transcript_num].split('\t')[1]
		transcript_line = transcript_line.replace('.', '')
		transcript_line = transcript_line.replace(',', '')
		transcript_line = transcript_line.replace('!', '')
		transcript_line = transcript_line.replace(':', '')
		transcript_line = transcript_line.replace('?', '')
		transcript_line = transcript_line.replace('\'', '')
		transcript_line = transcript_line.replace('\"', '')

		for t in transcript_line.split():
		  words_mlf.write('{0}\n'.format(t))
		
		words_mlf.write('.\n')




