#!/usr/bin/python

## Python script for creating Renderman texture from a sequence of tiff or targa files

import sys
import os

argc = len(sys.argv)
if not 1 <=  argc > 2:
    print "\n USAGE: txmakem.py inname fs (fe (fi (ext)))"
    print "          - inname - the basename of the input file"
    print "          - fs - framestart, assumes same frame if only arg"
    print "          - fe - frameend"
    print "          - fi - frame increment, assume 1"
    print "          - ext - (optiona)  the input file extension, assumes tif\n"
    sys.exit(0) 

## Catch input errors
## wrong number of args
if argc  < 4:
    print ''
    print "MVFRAMENAMES takes at least 3 arguments to run the script. Try again, please.\n"
    sys.exit(0)

if argc > 6:
    print ''
    print "MVFRAMENAMES take at most 5 arguments to run the script. Try again, please.\n"
    sys.exit(0)

## set input values
inname = sys.argv[1]
fs = int(sys.argv[2])
if argc >= 4:
    fe = int(sys.argv[3])
else: 
    fe = int(sys.argv[2])
if argc >= 5:
    fi = int(sys.argv[4])
else:
    fi = 1
if argc == 6:
    ext = sys.argv[5]
else:
    ext = 'tif'

## outfile_exists = os.path.exists(outname)
rman=os.environ.get("RMANTREE")
## print rman

while fs <= fe:
    wnum = "%04d" % fs
    print "The wnum value is: " + wnum+ "\n"
    infile = inname  + '.' + wnum + '.' + ext
    outfile = inname + '.' + wnum + '.' + 'tex'
    cmd=rman + '/bin/txmake -mode periodic -resize up' + ' ' + infile + ' ' + outfile
    print "Writing" + ' ' + outfile
    os.system(cmd)
    fs += fi
