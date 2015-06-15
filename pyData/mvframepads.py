#!/usr/bin/python

## Python script for moving from 1 number padding to another

import sys
import os

argc = len(sys.argv)
if not 1 <=  argc > 2:
    print "\n USAGE: mvframepads.py inname outname fs fe inpad outpad (fi (ext)))"
    print "          - inname - the basename of the input file"
    print "          - outname =  the basename of the output file"
    print "          - fs - framestart, assumes same frame if only arg"
    print "          - fe - frameend"
    print "          - inpad -- the padding of the numbers in the original files"
    print "          - outpad -- the padding of the numbers in the new files"
    print "          - fi - frame increment, assume 1"
    print "          - ext - (optiona)  the file extension, assumes tif\n"
    print ""
    print "     EXAMPLE: Given foo.1-100.exr, move it to foo.0001-0100.exr: "
    print ""
    print "     mvframepads.py foo foonew 1 100 1 4 1 exr "
    print ""
    print "     RESULT: foonew.0001-0100.exr, then use mvframenames to move"
    print "     the basename back to foo from foonew."
    print ""
    sys.exit(0)

## Catch input errors
## wrong number of args
if argc  < 7:
    print ''
    print "MVFRAMEPADS takes at least 7 arguments to run the script. Try again, please.\n"
    sys.exit(0)

if argc > 9:
    print ''
    print "MVFRAMEPADS take at most 9 arguments to run the script. Try again, please.\n"
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
    inpad = int(sys.argv[5])
else:
    inpad = 4
if argc >= 7:
    outpad = int(sys.argv[6])
else:
    outpad = 4
if argc >= 8:
    fi = int(sys.argv[7])
else:
    fi = 1
if argc == 9:
    ext = sys.argv[8]
else:
    ext = 'tif'

## outfile_exists = os.path.exists(outname)

while fs <= fe:
    informat = "%0" + str(inpad) + str("d")
    outformat = "%0" + str(outpad) + str("d")
    innum = informat % fs
    outnum = outformat % fs
    infile = inname  + '.' + innum + '.' + ext
    print ""
    print "CONVERTING: "
    print infile
    outfile = outname + '.' + outnum + '.' + ext
    print "TO: "
    print outfile
    os.rename(infile,outfile)
    fs += fi

