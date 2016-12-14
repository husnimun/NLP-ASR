#!/usr/bin/python


from os import listdir
from os.path import isfile, join, splitext

files = [f for f in listdir('./recording') if isfile(join('./recording', f))]

with open('data.scp', 'w') as scp_data:
    for file in files:
        filename, extension = splitext(file)
        if extension == '.wav':
            scp_data.write('recording/{0} {1}\n'.format(file, 'mfcc/' + filename + '.mfc'))
            