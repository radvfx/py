#!/usr/bin/python

## Python script for renumbering a sequence of files

import sys
import os

argc = len(sys.argv)
if not 1 <=  argc > 2:
    print "\n USAGE: mvframenums inname outname fs (fe (fi (ext)))"
    print "          - inname - the basename of the input file"
    print "          - outname =  the basename of the output file"
    print "          - fs - framestart, assumes same frame if only arg"
    print "          - fe - frameend"
    print "          - offset - the offset value from the original. Cannot be negative."
    print "          - fi - frame increment, assume 1"
    print "          - ext - (optiona)  the file extension, assumes tif\n"
    sys.exit(0) 

## Catch input errors
## wrong number of args
if argc  < 4:
    print ''
    print "MVFRAMENUMS takes at least 3 arguments to run the script. Try again, please.\n"
    sys.exit(0)

if argc > 7:
    print ''
    print "MVFRAMENUMS take at most 6 arguments to run the script. Try again, please.\n"
    sys.exit(0)

## set input values
inname = sys.argv[1]
outname = sys.argv[2]
fs = int(sys.argv[3])
if argc >= 5:
    fe = int(sys.argv[4])
else: 
    fe = int(sys.argv[3])
if argc >= 6:
    offset = int(sys.argv[5])
else:
    offset = 0
if argc >= 7:
    fi = int(sys.argv[6])
else:
    fi = 1
if argc == 8:
    ext = sys.argv[7]
else:
    ext = 'tif'

## outfile_exists = os.path.exists(outname)

while fs <= fe:
    wnum = "%04d" % fs
    offsetwnum = "%04d" % fs+offset
    print "The wnum value is: " + wnum+ "\n"
    infile = inname  + '.' + wnum + '.' + ext
    print infile
    outfile = outname + '.' + offsetwnum + '.' + ext
    print outfile
    os.rename(infile,outfile)
    fs += fi


