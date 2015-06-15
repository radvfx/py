#!/usr/bin/python

## Python script for renaming a sequence of file extensions

import sys
import os

argc = len(sys.argv)
if not 1 <=  argc > 2:
    print "\n USAGE: mvframeexts inname outname inext outext fs (fe (fi)))"
    print "          - inname - the basename of the input file"
    print "          - outname - the basename of the output file"
    print "          - inext =  the name of the input extension, assumes tif"
    print "          - outext - the name of the output extension"
    print "          - fs - framestart"
    print "          - fe - frameend, assumes framestart"
    print "          - fi - frame increment, assumes 1\n"
    sys.exit(0)

## Catch input errors
## wrong number of args
if argc  < 6:
    print ''
    print "MVFRAMEEXTS takes at least 5 arguments to run the script. Try again, please.\n"
    sys.exit(0)

if argc > 9:
    print ''
    print "MVFRAMEEXTS take at most 8 arguments to run the script. Try again, please.\n"
    sys.exit(0)

## set input values
inname = sys.argv[1]
outname = sys.argv[2]
inext = sys.argv[3]
outext = sys.argv[4]
fs = int(sys.argv[5])
if argc >= 7:
    fe = int(sys.argv[6])
else:
    fe = int(sys.argv[5])
if argc >= 8:
    fi = int(sys.argv[7])
else:
   fi = 1
if argc == 8:
   ext = sys.argv[7]
else:
   ext = 'tif'

## debug input
## print "inname=:",inname
## print "outname=:",outname
## print "inext=:",inext
## print "outext=:",outext
## print "fs=:",fs
## print "fe=:",fe
## print "fi=:",fi

## outfile_exists = os.path.exists(outname)

while fs <= fe:
    wnum = "%04d" % fs
    ## print "The wnum value is: " + wnum+ "\n"
    infile = inname  + '.' + wnum + '.' + inext
    outfile = outname + '.' + wnum + '.' + outext
    print " MOVING " + infile + " TO " + outfile + "\n"
    os.rename(infile,outfile)
    fs = fs + fi

