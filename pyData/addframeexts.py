#!/usr/bin/python

## Python script for adding an extension suffix to a sequence of files

import sys
import os

argc = len(sys.argv)
if not 1 <=  argc > 2:
    print "\n USAGE: addframeexts inname ext fs (fe (fi)))"
    print "          - inname - the basename of the input file"
    print "          - ext - the extension name to add"
    print "          - fs - framestart"
    print "          - fe - frameend, assumes framestart"
    print "          - fi - frame increment, assumes 1\n"
    sys.exit(0)

## Catch input errors
## wrong number of args
if argc  < 4:
    print ''
    print "MVFRAMEEXTS takes at least 3 arguments to run the script. Try again, please.\n"
    sys.exit(0)

if argc > 6:
    print ''
    print "MVFRAMEEXTS take at most 5 arguments to run the script. Try again, please.\n"
    sys.exit(0)

## set input values
inname = sys.argv[1]
ext = sys.argv[2]
fs = int(sys.argv[3])
if argc >= 4:
    fe = int(sys.argv[4])
else:
    fe = int(sys.argv[3])
if argc >= 5:
    fi = int(sys.argv[5])
else:
   fi = 1

## debug input
print "inname=:",inname
print "ext=:",ext
print "fs=:",fs
print "fe=:",fe
print "fi=:",fi

## outfile_exists = os.path.exists(outname)

while fs <= fe:
    wnum = "%04d" % fs
    ## print "The wnum value is: " + wnum+ "\n"
    infile = inname  + '.' + wnum
    outfile = inname + '.' + wnum + '.' + ext
    print " MOVING " + infile + " TO " + outfile + "\n"
    os.rename(infile,outfile)
    fs = fs + fi

