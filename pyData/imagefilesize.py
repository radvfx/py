#! /usr/bin/python

## imagefilesize --  a script for getting data about image filesizes

## import python and qt modules
import os,sys,string

## commands used for exterior tmpfile.txt
tmpdir = 'tmpdir.txt'
pwd = '/bin/pwd ' + '>> ' + tmpdir
cleantmpdir = '/bin/rm ' + tmpdir
tmpdir_exists = os.path.exists(tmpdir)
clean = '/bin/rm ' + "tmpfile.txt"

argc = len(sys.argv)

def USAGE():
    print"\n USAGE: filesize (path (ext))  - help"
    print"          path - the full pathname to the files.  No filenames needed. Assumes current directory './'"
    print"          -help - prints out this Usage.\n"

## Catch input errors
if len(sys.argv) > 3:
    print "\nfilesize takes only 1 arg.  Please try again.\n"

# print Usage
for line in sys.argv:
    helpargs = string.lower(line)
    if helpargs == '-h':
        print USAGE()
        sys.exit(0)
    if helpargs == '-help':
        print USAGE()
        sys.exit(0)
    if helpargs == '-H':
        print USAGE()
        sys.exit(0)
    if helpargs == '-HELP':
        print USAGE()
        sys.exit(0)

## debug input args
## if argc <= 1:
    ## print "0 arg:",sys.argv[0]
## if argc > 1:
    ## print "1 arg:",sys.argv[1]

## set input args
if tmpdir_exists:
    os.system(cleantmpdir)
else:
    os.system(pwd)
for line in map(lambda x: x[:-1], open(tmpdir).readlines()):
    dirpath = line
    os.system(cleantmpdir)

print "DIRPATHPWD:",dirpath
if argc <= 0:
    pass
elif argc > 1:
        dirpath = str(sys.argv[1])

## make sure paths end with "/"
if dirpath.endswith("/"):
    pass
else:
    dirpath = dirpath +  "/"
if dirpath.startswith("/"):
    pass
else:
    dirpath = "/" + dirpath

print "DIRPATH:",dirpath

## another Linux command
cmd = '/bin/ls -l ' + dirpath + '*' + ' >> ' + "tmpfile.txt"

## set default args
tmpfile = "tmpfile.txt"
graph = {}
dirsize = float(0.0)
valbig = float(0.0)
valsmall = float(1000000000.0)
framebig = int(-1000000000)
framesmall = int(1000000000)

# use Linux 'ls' to create a tmpfile of directory information
tmpfile_exists = os.path.exists(tmpfile)
if tmpfile_exists:
    os.system(clean)

cmd = os.system(cmd)

## get filesize data from tmpfile
for line in map(lambda x: x[:-1], open(tmpfile).readlines()):
    ## make all whitespace uniform
    a0 = str(line)
    a1 = a0.replace('   ',' ')
    a2 = a1.replace('  ',' ')
    ## turn line into list
    a = a2.split(" ")
    ## print "A:",a
    b = a[4:5]
    c = str(b)
    ci = c.find("[")
    d = float(c[ci+2:-2])
    if d > valbig:
        valbig = d #container for largest d value
    if d < valsmall:
        valsmall = d #container for smallest d value
    ## print "FILE SIZE:",d
    dirsize += d
    gdirsize = dirsize/1000000000 #express value in gigabytes
    print "GDIRSIZE:",gdirsize
    e = a[7:8] 
    f = str(e)
    g = f.split(".")
    ## print "E:",e
    ## print "F:",f
    ## print "G:",g
    h = g[1:2]
    ## print "H:",h
    i = str(h)
    j = i.find("[")
    k = i[j+2:-2]
    ## print "K:",k
    if str(k).startswith(" "):
        pass
    elif str(k).startswith("0"):
        k = int(k[+1:])
    else:
        k = int(k)
    if k > framebig:
        framebig = k
    if k < framesmall:
        framesmall = k
    print "FRAME #:",k
    ## create a dictionary of filenumbers and filesize
    ## graph[k] = d
print "GRAPH:",graph
frames = int(framebig) - int(framesmall)
print "THE LARGEST VALUE IS:",valbig
print "THE SMALLEST VALUE IS:",valsmall
print "THE LOWEST FRAME #:", framesmall
print "THE HIGHEST FRAME #:", framebig
print "THE TOTAL # OF FRAMES:", frames + 1
print "THE DIR SIZE IN GBYTES:",gdirsize

