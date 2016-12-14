#!/usr/bin/python

monophones = open('monophones0').read().splitlines()
template = open('hmm0/proto_template.txt').read()

with open('HMMDevs', 'w') as HMMDevs_file:
    for monophone in monophones:
        HMMDevs_file.write('~h "{0}"\n'.format(monophone))
        HMMDevs_file.write('{0}'.format(template))
