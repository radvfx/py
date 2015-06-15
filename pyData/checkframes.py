#!/usr/bin/python

## checkframes -- check for a series of files with 4pad numbers

import sys
import os
import string

argc = len(sys.argv)
if not 1 <= argc > 2:
    print "\n USAGE:	checkframes basename fs fe fi ext (-(n)ot, -(e)xists, -(l)ist)"
    print "		- basename of basename.%04d.ext"
    print "		- fs = the start frame"
    print "		- fe = the end frame"
    print "		- fi = the frame increment"
    print "		- ext = the file extension"
    print "		- (-(n)ot =does NOT exist, -(e)xists = exists, -(l)ist = print list)\n"
    sys.exit(0)

## catch input errors
if argc < 6 > 8:
    print"\n CHECKFRAMES takes 5 arguments to run.  Please try again.\n"
    sys.exit(0)

## set input values
basename = sys.argv[1]
fs = int(sys.argv[2])
fe = int(sys.argv[3])
fi = int(sys.argv[4])
ext = sys.argv[5]

## do it
fsnew = int(sys.argv[2])
incnum = 1
for line in sys.argv:
    flag = string.lower(line)
    if flag == '-n':
        while fs <= fe:
            wnum = "%04d" % fs
            file = basename + '.' + wnum + '.' + ext
            fileExists = os.path.exists(file)
            if not fileExists:
                print file
            fs += fi
    if flag == '-e':
        while fs <= fe:
            wnum = "%04d" % fs
            file = basename + '.' + wnum + '.' + ext
            fileExists = os.path.exists(file)
            if fileExists:
                print file
            fs += fi
    if flag == '-l':
        print "SHOW A LIST"
        while fsnew <= fe:
            wnum = "%04d" % int(fsnew)
	    nextnum = "%04d" % (int(fsnew) + 1)
	    prevnum = "%04d" % (int(fsnew) - 1)
            file = basename + '.' + wnum + '.' + ext
            prevfile = basename + '.' + prevnum + '.' + ext
            nextfile = basename + '.' + nextnum + '.' + ext
            fileExists = os.path.exists(file)
	    nextFileExists = os.path.exists(nextfile)
            if fileExists:
                if not nextFileExists:
                    startframe = "%04d" % int(incnum)
		    print basename + '.' + startframe + " - " + wnum + '.' + ext 
		    incnum = fs + int(int(wnum) + 1)
            fsnew += fi
