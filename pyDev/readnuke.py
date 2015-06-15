#!/usr/local/bin/python

## get all the paths of inputs/outputs used in a Nuke script
## script assume std prod setup 10-11-14

import sys
import os
import os.path
import string
import sets

def visit(data, dirname, files):
    return dirname

## print "The arg count is: %d" % len(sys.argv)

## if no args, print USAGE
if len(sys.argv) == 1:
    print "\n USAGE: readNuke.py show shot nk_file user (nk/online/diff/notdiff)"
    print "     show - show you are working on (eg. home, pbox, etc.)"
    print "     shot - the shot you wish to check"
    print "     bns_file - the name of the Nuke script"
    print "     user - the login name of the Nuke script maker"
    print "     diff/nk/online/notdiff - (optional) your output file will be:"
    print "         nk     - the dirs referecned by the Nuke script"
    print "         online  - the dirs online for the shot in subdirs '\comp' & '\rnd'"
    print "         diff    - the dirs on-line not referenced by the Nuke script, (assumes this)"
    print "         notdiff - the dirs referenced by the Nuke script that are not online"
    print " EXAMPLE: readNuke.py home exp01 exp01_comp_v22.nk jimbo\n"
    sys.exit(0)

## set input args
show = sys.argv[1] 
shot = sys.argv[2]
nk_file = sys.argv[3]
user = sys.argv[4]
output = 'diff'
if len(sys.argv) > 5:
    if sys.argv[5] == nk:
        output == nk
    else:
        output == online
else:
    pass

# where's the file?
file = '/shots/' + show + '/' + shot + '/comp/' + user + '/' + nk_file

# search which directories in that shot?
searchdirs = ('pix', 'comp')

## file exists?
file_exists = os.path.exists = (file)

## if the file exists, read it, and find all the input and output directory names
if file_exists:
    nk_set = sets.Set()
    online_set = sets.Set()
    for line in map(lambda x: x[:-1], open(file).readlines()):
        pattern = 'name_value'
        if pattern in line:
            i =  string.index(line, pattern)
            input = line[i+14:]
            nk_input = os.path.dirname(input)
            ## print "The nk_input is: " + nk_input
            nk_input = string.strip(nk_input)
            nk_set.add(nk_input)
    for line in searchdirs:
        subpix = line
        path = '/shots/%s/%s/%s/' % (show, shot, subpix)
        ## print "The searchpath is: " + path
        ## fileout= '/shots/' + show + '/' + shot + '/comp/' + user + '/' + shot + '_comp_unused.txt'
        ## file = open(fileout, 'w')
        ## compare every input line in Nuke script with directories on-line
        for root, dirs, files in os.walk(path):
            for line in dirs:
                dir_name = string.strip(line)
                online_dirs = root + '/' + dir_name
                online_set.add(online_dirs)
                ## print online_dir
                ## if online_dir == nk_input:
                    ## print "The matched path is: " + online_dir

## find the difference between the nk_set and the online_set
diff_set = online_set.difference(nk_set)
notdiff_set = nk_set.difference(online_set)

## open and write the output file
filename = path +  user + '/' + shot + '_comp_' + output + '.txt'
fileout = open(filename, 'w')
if output == 'online':
    output_set = online_set
elif output == 'nk':
    output_set = nk_set
elif output == 'notdiff'
    outpout_set = notdiff_set
else:
    output_set = diff_set

for line in output_set:
    fileout.write(line)
    fileout.write('\n')
sys.exit(0)
