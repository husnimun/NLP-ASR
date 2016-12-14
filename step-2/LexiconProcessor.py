#!/usr/bin/python

lines = open("lexicon.txt").read().splitlines()


with open('lexicon_new.txt', 'w') as lexicon_new:
    for line in lines:
        first, second = line.split(' ', 1)
        lexicon_new.write('{0}\t[{0}]\t{1}\n'.format(first, second))