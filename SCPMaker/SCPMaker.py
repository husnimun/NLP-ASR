#!/usr/bin/python


from os import listdir
from os.path import isfile, join, splitext

files = [f for f in listdir('.') if isfile(join('.', f))]

with open('data.scp', 'w') as scp_data:
    for file in files:
        filename, extension = splitext(file)
        if extension != '.py':
            scp_data.write('{0} {1}\n'.format(file, filename + '.mfc'))
            