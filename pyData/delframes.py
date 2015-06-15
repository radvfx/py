#!/usr/bin/python

## Python script for removing (del) a sequence of files

import sys
import os

argc = len(sys.argv)
if not 1 <=  argc > 2:
    print "\n USAGE: delframes basename fs (fe (fi (ext)))"
    print "          - basename - the basename of the input file -- before the sequential number"
    print "          - fs - framestart, assumes same frame if only arg"
    print "          - fe - frameend"
    print "          - fi - frame increment, assume 1"
    print "          - ext - (optiona)  the file extension, assumes exr\n"
    sys.exit(0)

## Catch input errors
## wrong number of args
if argc  < 4:
    print ''
    print "DELFRAMES takes at least 3 arguments to run the script. Try again, please.\n"
    sys.exit(0)

if argc > 7:
    print ''
    print "DELFRAMES take at most 6 arguments to run the script. Try again, please.\n"
    sys.exit(0)

## set input values
basename = sys.argv[1]
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
   ext = 'exr'

fs4 = "%04d" % fs
fe4 = "%04d" % fe
fi1 = "%01d" % fi
fis = fi1 + "s"

file = basename + "." + fs4 + "." + ext
allfiles = basename + "." + fs4 + "-" + fe4 + "." + ext
print "ALLFILES:",allfiles
print "FILE:",file

file_exists = os.path.exists(file)
if file_exists:
    response = raw_input("\nYou are about to remove " + allfiles + " on " + fis + ".  Is this okay? (y/n)")
    if response[0] in 'Yy':
        while fs <= fe:
            wnum = "%04d" % fs
            file = basename  + '.' + wnum + '.' + ext
            remove = '/bin/rm ' + file
            print " REMOVING " + file + "\n"
            os.system(remove)
            fs = fs + fi
else:
    print "\nThe file doesn't exist. Please try again.\n"
    sys.exit(0)
