#!/usr/local/bin/python2.3

## example of using os.walk

import os
import os.path
import sys
import string

show = 'sp2'
shot = 'nr01'
user = 'jhillin'
bnsfile = 'nr01_comp_v22.bns'
subdirs = ('pix','comp')

for line in subdirs:
    path = '/shots/' + show + '/' + shot + '/' +  line
    print path
    for root, dirs, files in os.walk(path):
        for line in dirs:
            dir_name = string.strip(line)
            print root + '/' + dir_name
    sys.exit(0)    
