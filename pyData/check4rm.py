evalfile.py                                                                                         0100777 0021522 0000024 00000001170 10037555403 012411  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

import os,sys
import string

print """
	Let's see:  Did you call this file "prodlist.txt"?
	"""

file_exists = os.path.exists("prodlist.txt")

if file_exists:
    response = raw_input("Yes, you did.  Do you want to display the file now? (y/n) ")
    if response[0] in 'Yy':
        for line in map(lambda x: x[:-1], open("prodlist.txt").readlines()):
            print line #prints only the first line
    else:
        print '\nOK.'
	print "" ## blank line

## sys.exit(0)


## word lengths
word_lengths = "map(lamda x: map(len, x), file_exists)"
print word_lengths, '=>'
print '  ', eval(word_lengths)
                                                                                                                                                                                                                                                                                                                                                                                                        foo.py                                                                                              0100777 0021522 0000024 00000000127 10043252430 011375  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

x = 9
print x

if x <= 9:
    print "less than %d" % (x)


                                                                                                                                                                                                                                                                                                                                                                                                                                         getopt.py                                                                                           0100777 0021522 0000024 00000001012 10033402005 012100  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   $!/usr/local/bin/python2.3

import getopt, sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError:
        # print help information and exit:
	usage()
	sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
	    verbose = True
        if o in ("-h", "--help"):
	    usage()
	    sys.exit()
        if o in ("-o", "--output"):
	    output = a
        else
	    pass

if __name__ == "__main__":
    main()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      getstockquote.py                                                                                    0100777 0021522 0000024 00000001423 10043252135 013515  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

import urllib
import string

def getstockquote( symbol ):
    'print stock symbol latest price quote from http://cnn.money.com'
    url = urllib.urlopen('http://quote.money.cnn.com/quote/quote?symbols=' + symbol)
    for line in url.readlines():
        if 'td class' in line:
                i = string.index(line, 'td class')
                quote = line[i+29:i+34]
                print '' ## empty line
                print '"The Latest Stock Price for" %s "is" %s' % (symbol,quote)
                print '' ## empty line
                break

if __name__ == '__main__':
    print''
    symbol = input('Which stock symbol would you like quoted?\n'
                   '(NOTE: stock symbol must be in quotes)     ')
    print ''
    getstockquote(symbol)
                                                                                                                                                                                                                                             hello.py                                                                                            0100777 0021522 0000024 00000000060 10033114650 011711  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

print "Hello World"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                loopargex.py                                                                                        0100777 0021522 0000024 00000001113 10045527406 012620  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

import sys
import string

def HELP():
    return "\n HELP: \n"

def FULLHELP():
    return "\n FULLHELP:\n" 

## print sys.argv
for line in sys.argv:
    lcargs = string.lower(line)
    print lcargs
    if lcargs == '-h':
        print HELP()
    elif lcargs == '-help':
        print HELP()
    elif lcargs == '-f':
        print FULLHELP()
    elif lcargs == '-fullhelp':
        print FULLHELP()
    elif not 1 < len(sys.argv) < 7:
        print "\n USAGE: matchbns.py bns_file (show (shot (user (bns/online/diff/notdiff))))\n"
        sys.exit(0)

    


                                                                                                                                                                                                                                                                                                                                                                                                                                                     loopsysargv.py                                                                                      0100777 0021522 0000024 00000003577 10045544141 013223  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

import sys
import string

def HELP():
    return "\n USAGE:  matchbns.py bns_file (show (shot (user (bns/online/diff/notdiff))))\n" "         For more information, use -fullhelp.\n"

def FULLHELP():
    return "\n FULLHELP: matchbns.py bns_file (show (shot (user (bns/online/diff/notdiff))))\n" "\n NOTE:  Please setshot to use this script.\n" "     bns_file - the name of the bonsai script\n" "     show - (optional) show you are working on (eg. sp2, pex, etc.), assumes $SHOW\n" "     shot - (optional) the shot you wish to check, assumes $SHOT\n" "     user - (optional) the login name of the bonsai script maker, assumes $USER\n"  "     diff/bns/online/notdiff - (optional) your output file will be:\n" "         bns     - the dirs referecned by the bonsai script (same as check-bns)\n" "        online  - the dirs online for the shot in subdirs 'pix' & 'comp'\n" "         diff    - the dirs on-line not referenced by the bonsai script, (assumes this)\n" "         diff    - the dirs on-line not referenced by the bonsai script, (assumes this)\n" "         notdiff - the dirs referenced by the bonsai script that are not online\n" "\n" " EXAMPLE: matchbns.py nr01_comp_v22.bns sp2 nr01 jhillin\n" "\n" " This will write a txt file named <shotname>_comp_<output>.txt to your comp/<user>\n" " directory containing a list of the directories referenced.\n" "\n"

## print sys.argv
for line in sys.argv:
    lcargs = string.lower(line)
    print lcargs
    if lcargs == '-h':
        print HELP()
    elif lcargs == '-help':
        print HELP()
    elif lcargs == '-f':
        print FULLHELP()
    elif lcargs == '-fullhelp':
        print FULLHELP()
    elif lcargs == '-stdout':
        output = 'stdout' 
        print output
    elif not 1 < len(sys.argv) < 7:
        print "\n USAGE: matchbns.py bns_file (show (shot (user (bns/online/diff/notdiff))))\n"
        sys.exit(0)

    


                                                                                                                                 looptest.py                                                                                         0100777 0021522 0000024 00000000422 10045013152 012457  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

import os
import sys

fs = int(sys.argv[1])
print type(fs)
fe = int(sys.argv[2])
fi = int(sys.argv[3])


## fs = 1
## print type(fs)
## fe = 5
## fi = 1

nums = range(fs,fe + 1,fi)
for line in nums:
    wnum = "%04d" % line
    print wnum + '\n'
                                                                                                                                                                                                                                              matchbns.py                                                                                         0100777 0021522 0000024 00000015546 10045546261 012436  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

## matchbns.py -- compares the input/output directorieis of a bonsai script with
##                the available online directories of the script's shot.  Matchbns.py
##                will write a text file to the shot's comp/<user> directory with 
##                the desired information in a list.
##
##                The 'output' list can contain either:
##                diff    - what is online that is not referenced by the bonsai script (assumes this)
##                bns     - what the bonsai script references (just like check-bns)
##                online  - what directories exist in the shot's 'pix' and 'comp' directories
##                notdiff - what the bonsai script references that is no longer online
##
##                Respectively, the filenames will be <shotname>_comp_<output>.txt


import sys
import os
import os.path
import string
import sets

def visit(data, dirname, files):
    return dirname

def HELP():
    return "\n USAGE:  matchbns.py bns_file (show (shot (user (bns/online/diff/notdiff (stdout)))))\n" "         (For more information, use -(f)ullhelp.)\n"

def FULLHELP():
    return "\n FULLHELP: matchbns.py bns_file (show (shot (user (bns/online/diff/notdiff))))\n" "\n NOTE:  You do not need setshot to use this script, however, some of its\n" "        assumptions will fail, if it is not set.\n" "\n     bns_file - the name of the bonsai script\n" "     show - (optional) show you are working on (eg. sp2, pex, etc.), assumes $SHOW\n" "     shot - (optional) the shot you wish to check, assumes $SHOT\n" "     user - (optional) the login name of the bonsai script maker, assumes $USER\n"  "     diff/bns/online/notdiff - (optional) your output file will be:\n" "         - bns     - the dirs referecned by the bonsai script (same as check-bns)\n" "         - online  - the dirs online for the shot in subdirs 'pix' & 'comp'\n" "         - diff    - the dirs on-line not referenced by the bonsai script, (assumes this)\n" "         - notdiff - the dirs referenced by the bonsai script that are not online\n" "\n" "    stdout - if this argument is present, the information will be printed to STDOUT.\n" "\n EXAMPLE: matchbns.py nr01_comp_v22.bns sp2 nr01 jhillin\n" "\n" " This will write a txt file named <shotname>_comp_<output>.txt to your comp/<user>\n" " directory containing a list of the directories referenced. Unless stdout is set.\n" "\n"

## catch input errors
if len(sys.argv) > 6:
    print "\n matchbns.py  takes at most 5 arguments to run. Try again, please.\n"
    sys.exit(0)

## print sys.argv
for line in sys.argv:
    helpargs = string.lower(line)
    if helpargs == '-h':
        print HELP()
        sys.exit(0)
    elif helpargs == '-help':
        print HELP()
        sys.exit(0)
    elif helpargs == '-f':
        print FULLHELP()
        sys.exit(0)
    elif helpargs == '-fullhelp':
        print FULLHELP()
        sys.exit(0)
    elif not 1 < len(sys.argv) < 7:
        print "\n USAGE: matchbns.py bns_file (show (shot (user (bns/online/diff/notdiff (stdout)))))\n"
        print "  EXAMPLE:  matchbns.py nr01_comp_v11.bns sp2 nr01 jhillin"
        print "                (For more information, use -(f)ullhelp)\n"
        sys.exit(0)


## set input args
bns_file = sys.argv[1]
if len(sys.argv) < 3:
    show = os.environ['SHOW']
else:
    show = sys.argv[2] 

if len(sys.argv) < 4:
    shot = os.environ['SHOT']
else:
    shot = sys.argv[3]

if len(sys.argv) < 5:
    user = os.environ['USER']
else:
    user = sys.argv[4]

output = 'diff'
if len(sys.argv) > 5:
    output = sys.argv[5]
    print "\n The output is: %s" % output

# where's the file?
file = os.path.join('/shots', show, shot, 'comp', user, bns_file)

# search which directories in that shot?
searchdirs = ('pix', 'comp')

## bonsai script exists?
script_exists = os.path.exists(file)

## if the file exists, read it, and find all the input and output directory names
if script_exists:
    bns_set = sets.Set()
    online_set = sets.Set()
    for line in map(lambda x: x[:-1], open(file).readlines()):
        pattern = 'name_value'
        if pattern in line:
            i =  string.index(line, pattern)
            input = line[i+14:]
            bns_input = os.path.dirname(input)
            bns_input = string.strip(bns_input)
            bns_set.add(bns_input)
    for line in searchdirs:
        subpix = line
        path = os.path.join('/shots', show, shot, subpix)
        for root, dirs, files in os.walk(path):
            for line in dirs:
                dir_name = string.strip(line)
                online_dirs = root + '/' + dir_name
                online_set.add(online_dirs)

    ## find the difference between the bns_set and the online_set
    diff_set = online_set.difference(bns_set)
    notdiff_set = bns_set.difference(online_set)

    ## open and write the output file
    ## print "The path for fileout is: %s" % path
    filename = path + '/' +  user + '/' + shot + '_comp_' + output + '.txt'
    print "\n The path and output file is: %s " % filename
    filename_exists = os.path.exists(filename)
    if filename_exists:
        response = raw_input("\n The output file exists.  Do you want to overwrite it? (y/n) ")
        if response[0] in 'Yy':
            fileout = open(filename, 'w')
            if output == 'online':
                output_set = online_set
            elif output == 'bns':
                output_set = bns_set
            elif output == 'notdiff':
                output_set = notdiff_set
            else:
                output_set = diff_set

            ## if stdout not requested
            if output_mode != 'stdout':
                ## write the file header and the file
                if output == 'bns':
                    bns_hdr = "## bns_file header: These are the directories referenced by the Bonsai script: " + bns_file + "\n"
                    fileout.write(bns_hdr)
                elif output == 'online':
                    online_hdr = "## online file header: These are the pix and comp directories available in the shot: " + shot + "\n"
                    fileout.write(online_hdr)
                elif output == 'notdiff':
                    notdiff_hdr = "## notdiff file header: These directories are NOT online that are referenced by the Bonsai script: " + bns_file + "\n"
                    fileout.write(notdiff_hdr)
                else:
                    diff_hdr = "## diff file header:  These directories are online and not referenced by the Bonsai script: " + bns_file + "\n"
                    fileout.write(diff_hdr)

                for line in output_set:
                    fileout.write(line)
                    fileout.write('\n')
            else:
                # send to stdout
                for line in output_set:
                    print line
        else:
            print "\n Output file exists. Output halted.\n"
            sys.exit(0)
else:
    print "\n %s doesn't exist.  Please check and try again.\n" % file
                                                                                                                                                          mathdefs.py                                                                                         0100666 0021522 0000024 00000000414 10042557354 012415  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

def sum(x, y):
    'returns the sum'
    return x + y

def subtract(x,y):
    'returns the difference'
    return x - y

def mult(x,y):
    'returns the multiple'
    return x * y

def divide(x,y):
    'returns the dividend'
    return x/y
                                                                                                                                                                                                                                                    mvframenames.py                                                                                     0100777 0021522 0000024 00000003167 10045514776 013322  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

## Python script for renaming a sequence of files

import sys
import os

argc = len(sys.argv)
print argc
if not 1 <=  argc > 2:
    print "\n USAGE: mvframenames inname outname fs (fe (fi (ext)))"
    print "          - inname - the basename of the input file"
    print "          - outname =  the basename of the output file"
    print "          - fs - framestart, assumes same frame if only arg"
    print "          - fe - frameend"
    print "          - fi - frame increment, assume 1"
    print "          - ext - (optiona)  the file extension, assumes rla\n"
    sys.exit(0) 

## Catch input errors
## wrong number of args
if argc  < 4:
    print ''
    print "MVFRAMENAMES takes at least 3 arguments to run the script. Try again, please.\n"
    sys.exit(0)

if argc > 7:
    print ''
    print "MVFRAMENAMES take at most 6 arguments to run the script. Try again, please.\n"
    sys.exit(0)

## set input values
inname = sys.argv[1]
outname = sys.argv[2]
fs = int(sys.argv[3])
if argc == 5:
    fe = int(sys.argv[4])
else: 
    fe = int(sys.argv[3])
if argc == 6:
    fi = int(sys.argv[5])
else:
    fi = 1
if argc == 7:
    ext = sys.argv[6]
else:
    ext = 'rla'

def movefile(infile, outfile):
    print '\n MOVING  ' + infile + '  TO  ' + outfile + '\n'
    cmd = "/bin/mv &"
    ## os.system(cmd) infile outfile

outfile_exists = os.path.exists(outname)

while fs <= fe:
    wnum = "%04d" % fs
    print "The wnum value is: " + wnum+ "\n"
    infile = inname  + '.' + wnum + '.' + ext
    print infile
    outfile = outname + '.' + wnum + '.' + ext
    print outfile
    ## movefile(infile,outfile)
    fs += fi

                                                                                                                                                                                                                                                                                                                                                                                                         myprog.py                                                                                           0100777 0021522 0000024 00000000431 10043253164 012132  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

import sys


x =  sys.argv[0]
inname = x
print "x = " +  x
print "inname = " + inname
y =  sys.argv[1]
print "y = " + y
z =  sys.argv[2]
print "z = " + z
zz =  sys.argv[3]
print "zz = " + zz

xx = len(sys.argv)
print "the number of args is: %d" % (xx)

                                                                                                                                                                                                                                       old_python_examples.py                                                                              0100777 0021522 0000024 00000013471 10037555133 014706  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

# I was using a string as a comment.  In fact, the first comment in a
# module is its documentation.

print """
The "map" function is based on Lisp, and executes the function on
corresponding arguments from the list(s) in turn.  For example, to
make floats out of a list of integers, you can map the "float"
function to the list.
"""

some_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# or better, using the "range" function:

some_ints = range(1,13) # List goes up to one less than the second argument.

print 'Here\'s our list, called "some_ints":'
print some_ints

print '\nThis is what "map(float, some_ints)" does:'
print map(float, some_ints)

print """
You can make up your own functions The "lambda" syntax is a weak
version of its Lisp inspiration, but it's still incredibly handy. You
can get a new list from any number of lists.  Let's say you want to
add two lists together:
"""

list_1 = range(1,11)
list_2 = range(101, 111)

print "Here's list_1:" # Either ' or " work for strings.
print list_1

print "\nHere's list_2:"  
print list_2

print '\nSo you can add them with "map(lambda x,y: x+y, list_1, list_2)"'

print map(lambda x,y: x+y, list_1, list_2)

print """
The "reduce" function calls its function argument on the result of the
previous evaluation of the function and the next element in the list
(just like Lisp again).  You use lambda to make functions out of
operators. For example, to sum up a list you use the lambda syntax to
make a function out of the "+" operator: """

print "\nreduce(lambda x,y: x+y, list_1) =>", reduce(lambda x,y: x+y, list_1)

print "\nAnd these can be combined endlessly (but don't turn it into Perl):"

example = "reduce(lambda x,y: x+y, map(lambda x,y: x+y, list_1, list_2))"
# Here's how you do string formatting (and it's about time I used "eval"...):
print '\n%s => %g\n' % (example, eval(example)) 

# YOU WOUDN'T NORMALLY USE EVAL MUCH, but it's handy for these examples.

some_data = """
When you need a list of data that you want to represent cleanly in a
file, you can use the "triple quotation mark" syntax, and then treat
the string like an object, stripping and splitting it.  This makes it
easy to enter data in a file and not worry about the formatting
syntax.  """.strip().split('\n')   # The string is an object!

for line in some_data:
    print line


some_more_data = """
This data can be formatted
in arbitrary ways with any
list structure by mapping a
splitting function on the list
""".strip().split('\n')

print # Just a newline.
for line in some_more_data:
    print line

# Normally you import modules at the head of the file, but for clarity
# I'm not doing it now until I need it:
import string

# Remember what I said about the first string of a module being it's
# documentation?  Start Python and try this:
#    import string
#    print string.__doc__

# The variables with '__' around them are special, and include the
# filename from which the module was loaded.  To see all the symbols
# loaded by a module, try this:
#    import string
#    dir(string)


some_more_data = map(lambda x: string.split(x), some_more_data)
print
for line in some_more_data:
    print line

print """
And now, putting this all together, what's the longest word in each
line?

First, the lengths of the words in each line:
"""

word_lengths = "map(lambda x: map(len, x), some_more_data)"
print word_lengths, '=>'
print '  ', eval(word_lengths)  # Indenting for clarity
print '\nNow we can reduce each line to its maximum:\n'

line_max_lengths = "map(lambda x: reduce(max, map(len, x)), some_more_data)"

print line_max_lengths, '=>'
print '  ' , eval(line_max_lengths)


print "\nHey, wait, are they all equal?  If they are, then they're all equal to the first one:\n"

lengths = eval(line_max_lengths)
print 'lengths = %s' % (lengths)  # The "%s" formats the list like you expect.
# Can't use eval because of assignment to variable.
print 'map(lambda x,y: x==y, [lengths[0]]*len(lengths), lengths) =>', # Comma means no newline.
print map(lambda x,y: x==y, [lengths[0]]*len(lengths), lengths)

print '\nIf we reduce that, we get the single answer:\n'

print 'reduce(lambda x,y: x==y, map(lambda x,y: x==y, [lengths[0]]*len(lengths), lengths)) =>',
print reduce(lambda x,y: x==y, map(lambda x,y: x==y, [lengths[0]]*len(lengths), lengths))

print """
Of course you can use temporary variables for intermediate stages, but
sometimes the combined form is the clearest expression of your
intended meaning.
	    """

print 'Notice that "<sequence>*N" repeats the sequence N times.\n'

print '-+*+' * 17 + '-'  # Notice * and + are both defined for strings.

print """
What about reading files?  Since the "open" function returns an
object, you can call the string method "readlines" directly on it.  We
already know about mapping a function on a list, so I can open a file,
read all the lines, and strip the final newline, all at once.
Subscripts that are negative numbers count from the end of the list or
string, so "x[:-1]" means "all elements in the list except the last
one".

Try this on a file called "filename":

        for line in map(lambda x: x[:-1], open("filename").readlines()):
	        print line

		Let's see: did you call this file "python_examples.py"?
		"""

import os, sys  # Normally, at the beginning.
file_exists = os.path.exists("python_examples.py")

if file_exists:
    response = raw_input("Yes, you did. Do you want to display the file now? (y/n) ")
    if response[0] in 'Yy':   # The "in" operator works for lists AND strings!
        for line in map(lambda x: x[:-1], open("python_examples.py").readlines()):
            print line
	    ## sys.exit(0)  # This is how you terminate execution.
    else:
        print '\nOK.',  # Comma prevents newline.
	print ""  ## blank line
    ### else:
        ###    print 'No, you put it somewhere else.',

        ###  print 'Check out the file reading code at the end of it.'


                                                                                                                                                                                                       options.py                                                                                          0100777 0021522 0000024 00000000342 10033400551 012302  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                    #!/usr/local/bin/python2.3
 
 from optparse import OptionParser

 parser = OptionParser()
 parser.add_option("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE")
 (options,args) = parser.parse_args()
                                                                                                                                                                                                                                                                                              printfile.py                                                                                        0100777 0021522 0000024 00000001336 10037553622 012623  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

import os,sys
import string

print"" ## skip a line
some_more_data = os.path.exists("prodlist.txt")
for line in map(lambda x: x[:-1], open("prodlist.txt").readlines()):
    print line
print "" ## skip a line

some_more_data = "bob, sally, julie, jim"

print some_more_data

some_more_data = map(lambda x: string.split(x), some_more_data)
print ""
for line in some_more_data:
    print line

word_lengths = "map(lambda x: map(len, x), some_more_data)"
print word_lengths, '=>'
print '  ', eval(word_lengths)
print '\nNow we can reduce each line to its maximum:\n'

line_max_lengths = "map(lambda x: reduce(max, map(len, x)), some_more_data)"

print line_max_lengths, '=>'
print '  ', eval(line_max_lengths)
                                                                                                                                                                                                                                                                                                  readbns.py                                                                                          0100777 0021522 0000024 00000006631 10044244453 012245  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

## get all the paths of inputs/outputs used in a bonsai script (like check-bns)

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
    print "\n USAGE: readbns.py show shot bns_file user (bns/online/diff/notdiff)"
    print "     show - show you are working on (eg. sp2, pex, etc.)"
    print "     shot - the shot you wish to check"
    print "     bns_file - the name of the bonsai script"
    print "     user - the login name of the bonsai script maker"
    print "     diff/bns/online/notdiff - (optional) your output file will be:"
    print "         bns     - the dirs referecned by the bonsai script"
    print "         online  - the dirs online for the shot in subdirs '\comp' & '\rnd'"
    print "         diff    - the dirs on-line not referenced by the bonsai script, (assumes this)"
    print "         notdiff - the dirs referenced by the bonsai script that are not online"
    print " EXAMPLE: readbns.py sp2 nr01 nr01_comp_v22.bns jhillin\n"
    sys.exit(0)

## set input args
show = sys.argv[1] 
shot = sys.argv[2]
bns_file = sys.argv[3]
user = sys.argv[4]
output = 'diff'
if len(sys.argv) > 5:
    if sys.argv[5] == bns:
        output == bns
    else:
        output == online
else:
    pass

# where's the file?
file = '/shots/' + show + '/' + shot + '/comp/' + user + '/' + bns_file

# search which directories in that shot?
searchdirs = ('pix', 'comp')

## file exists?
file_exists = os.path.exists = (file)

## if the file exists, read it, and find all the input and output directory names
if file_exists:
    bns_set = sets.Set()
    online_set = sets.Set()
    for line in map(lambda x: x[:-1], open(file).readlines()):
        pattern = 'name_value'
        if pattern in line:
            i =  string.index(line, pattern)
            input = line[i+14:]
            bns_input = os.path.dirname(input)
            ## print "The bns_input is: " + bns_input  ## to here, same as check-bns
            bns_input = string.strip(bns_input)
            bns_set.add(bns_input)
    for line in searchdirs:
        subpix = line
        path = '/shots/%s/%s/%s/' % (show, shot, subpix)
        ## print "The searchpath is: " + path
        ## fileout= '/shots/' + show + '/' + shot + '/comp/' + user + '/' + shot + '_comp_unused.txt'
        ## file = open(fileout, 'w')
        ## compare every input line in bonsai script with directories on-line
        for root, dirs, files in os.walk(path):
            for line in dirs:
                dir_name = string.strip(line)
                online_dirs = root + '/' + dir_name
                online_set.add(online_dirs)
                ## print online_dir
                ## if online_dir == bns_input:
                    ## print "The matched path is: " + online_dir

## find the difference between the bns_set and the online_set
diff_set = online_set.difference(bns_set)
notdiff_set = bns_set.difference(online_set)

## open and write the output file
filename = path +  user + '/' + shot + '_comp_' + output + '.txt'
fileout = open(filename, 'w')
if output == 'online':
    output_set = online_set
elif output == 'bns':
    output_set = bns_set
elif output == 'notdiff'
    outpout_set = notdiff_set
else:
    output_set = diff_set

for line in output_set:
    fileout.write(line)
    fileout.write('\n')
sys.exit(0)
                                                                                                       readfile.py                                                                                         0100777 0021522 0000024 00000000767 10037554664 012420  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

import os,sys
import string

print """
	Let's see:  Did you call this file "prodlist.txt"?
	"""

file_exists = os.path.exists("prodlist.txt")

if file_exists:
    response = raw_input("Yes, you did.  Do you want to display the file now? (y/n) ")
    if response[0] in 'Yy':
        for line in map(lambda x: x[:-1], open("prodlist.txt").readlines()):
            print line #prints only the first line
    else:
        print '\nOK.'
	print "" ## blank line

## sys.exit(0)

         some_data.py                                                                                        0100777 0021522 0000024 00000000161 10037552204 012551  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

import os,sys
import string

some_data = """
bob
sally
julie
jim
"""
print some_data
                                                                                                                                                                                                                                                                                                                                                                                                               spref.py                                                                                            0100777 0021522 0000024 00000000337 10033342266 011742  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

product = 'chr_hit.pit'
version = 3
spref = 'spref_eval "{' + product + "?ver=" + str(version) + '}"'
print spref

spref2 = 'spref_eval "{' + "%s?ver=%d" % (product,version) + '}"'
print spref2

                                                                                                                                                                                                                                                                                                 stocks.py                                                                                           0100777 0021522 0000024 00000002136 10046272211 012124  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

import sys
from qt import *

class StockWidget(QVBox):
    def __init__(self,parent=None,name=None):
        QVBox.__init__(self,parent,name)

        ## Make a button
        quit = QPushButton("Quit",self,"quit")
        quit.setFont(QFont("Times",18,QFont.Bold))
        self.connect(quit,SIGNAL("clicked()"),qApp,SLOT("quit()"))

        ## Make an editable line
        self.input = QVBox(self)
        lineedit = QLineEdit(self)
        lineedit.setText('Edit This')
        self.connect(lineedit,SIGNAL('textChanged(const QString&)'),qApp,SLOT("guiThreadAwake()"))

        def __textChanged(self, newTextQStr):
            newText = str(newTextQStr)
            print 'The new text is:', newText
            lineedit.setText(newText)

        ## Make a slider
        lcd = QLCDNumber(2,self,"lcd")
        slider = QSlider(Qt.Horizontal,self,"slider")
        slider.setRange(0,99)
        slider.setValue(0)

        self.connect(slider,SIGNAL("valueChanged(int)"),lcd,SLOT("display(int)"))

a = QApplication(sys.argv)

w = StockWidget()
a.setMainWidget(w)
w.show()
a.exec_loop()
                                                                                                                                                                                                                                                                                                                                                                                                                                  stringdefs.py                                                                                       0100666 0021522 0000024 00000000127 10042573542 012770  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

def getstr(x):
    'returns the string'
    return(x(str))
                                                                                                                                                                                                                                                                                                                                                                                                                                         testarg.py                                                                                          0100777 0021522 0000024 00000000243 10044253454 012272  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

import sys

usage = sys.argv[0]
if usage == 'testarg.py':
    print "\n USAGE: testarg.py du du du\n"

noarg = sys.argv[1]
print noarg
                                                                                                                                                                                                                                                                                                                                                             Tkwidget.py                                                                                         0100777 0021522 0000024 00000000201 10045510374 012373  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

from Tkinter import *

widget = Label(None, text='Hi, Im a widget!')
widget.pack()
widget.mainloop()
                                                                                                                                                                                                                                                                                                                                                                                               trythis.py                                                                                          0100777 0021522 0000024 00000001370 10043527415 012331  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

## Print out a file of a list of all possible images
## related to a shot's bonsai script.

import sys
import os
import os.path

def matchline(line1, line2):
    if line1 != line2:
        print line2
    else:
        pass

def visit(data, dirname, files):
    print dirname
    ## matchline(dirname,bnsdir)

show = 'sp2'
shot = 'nr01'
user = 'jhillin'
dirs = ('pix','comp')

for line in dirs:
    subpix = line
    path = '/shots/%s/%s/%s/' % (show, shot, subpix)
    print "The path is: %s" % path
    filename = '/shots/' + show + '/' + shot + '/comp/' + user + '/' +  shot + 'comp_unused.txt'
    fileout = open(filename, 'w')
    os.path.walk(path, visit, None)
    ## file.write(stdout)
    file.close(fileout)
sys.exit(0)


                                                                                                                                                                                                                                                                        walkpath.py                                                                                         0100777 0021522 0000024 00000000727 10043542372 012442  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   #!/usr/local/bin/python2.3

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
                                         bns_set.txt                                                                                         0100666 0021522 0000024 00000011422 10044232761 012441  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   /shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_nokey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_bty_key_only_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_spine_led_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_bty_key_only_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_nokey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_girder_key_cast_shadows_v1/2kfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_bty_key_only_v1/tvfa_lg16
/shots/sp2/op04/pix/plates/op04_bg_v2/tvfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_rkey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/mattes/op04_ock_mtt_v1/2kfa_lg8
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_spine_led_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_spine_led_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_bty_v1/2kfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_cam_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_rkey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_spine_led_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_nokey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_floor_contact_v1/tvfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_rkey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_bty_key_only_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_girder_key_cast_shadows_v1/tvfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_rkey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_cam_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_bty_v1/tvfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_spine_led_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_bty_key_only_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_spcl_lgt_only_cam_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_floor_key_cast_shadows_v1/2kfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_contact_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_spine_led_bty_v1/2kfa_lg16
/shots/sp2/reference/pix/out/op07/final/op07_comp_v9/tvfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_floor_key_cast_shadows_v1/tvfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_nokey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_rkey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_bty_key_only_v1/2kfa_lg16
/shots/sp2/op04/pix/plates/op04_bg_v2/2kfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_spine_led_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_rkey_bty_v1/2kfa_lg16
/shots/sp2/reference/pix/out/op07/final/op07_comp_v9/2kfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_rkey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_cam_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_rkey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_spine_led_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_floor_contact_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_cam_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_rkey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_floor_contact_v1/2kfa_nc16
/shots/sp2/op04/pix/mattes/op04_ock_mtt_v1/tvfa_lg8
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_bty_key_only_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_cam_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_contact_v1/tvfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_rkey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_nokey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_nokey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_floor_skylight_cast_shadows_v1/2kfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_cam_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/out/op04_comp_v19/2kfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_rkey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_rkey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_spcl_lgt_only_cam_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_nokey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_cam_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_floor_contact_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_floor_contact_v1/tvfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_bty_key_only_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_cam_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_nokey_bty_v1/tvfa_lg16
                                                                                                                                                                                                                                              names.txt                                                                                           0100666 0021522 0000024 00000000024 10037552241 012103  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   bob
sally
julie
jim
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            online_set.txt                                                                                      0100666 0021522 0000024 00000060265 10044232674 013157  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   /shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_bty_key_only_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_depth_v1/2kfa_ncf
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_rkey_v1/256sq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_rkey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_nokey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/ref/op04_anim_ref_v1/tvfa_bi8
/shots/sp2/op04/pix/mattes/op04_floorcloth2_matte_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_bty_key_only_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_skylight_v1/2ksq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_rkey_alt_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_rfl_lf_lwr_v1/2kfa_nc16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_lf_upr_sd_envdir_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_lf_upr_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_rkey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_bty_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_rt_upr_sd_envdir_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_nokey_bty_v1
/shots/sp2/op04/pix//pnt
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_floor_skylight_cast_shadows_v1/2kfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_cam_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_rfl_lf_lwr_v1/2kfa_nc16
/shots/sp2/op04/pix/pnt/op04_ock_comp_test_v1/tvfa_lg10
/shots/sp2/op04/pix//m2v
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_rt_lwr_dclaw_spcl_lgt_v1/2ksq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_rfl_lf_lwr_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_depth_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_cam_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_bty_stop_up_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_rt_lwr_sd_envdir_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_spine_led_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_rkey_alt_bty_v2/2kfa_lg16
/shots/sp2/op04/pix/mattes/op04_floorcloth_matte_v2/2kfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_nokey_bty_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_lscr_fill_v2/2ksq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_cam_bty_v1
/shots/sp2/op04/pix/maya/op04_lgrane_anim_render_v82
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/out/op04_mstokes_comp_bg_v1/2kfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_spcl_lgt_only_cam_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_rt_upr_sd_envdir_v1
/shots/sp2/op04/pix/out/video/thu2004apr29
/shots/sp2/op04/pix/pnt/op04_bg2_pnt_v2/2kfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_nokey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_bty_stop_up_v1/2kfa_lg16
/shots/sp2/op04/pix/out/op04_comp_v20/tvfa_lg10
/shots/sp2/op04/pix//maya
/shots/sp2/op04/pix/mattes/op04_floorcloth2_matte_v1/2kfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_spcl_lgt_cam_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_hinge_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_bty_stop_up_v1
/shots/sp2/op04/pix/plates/op04_bg_v2/2kfa_lg10
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_rt_lwr_dclaw_spcl_lgt_v1/256sq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_led_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_rt_lwr_dclaw_spcl_lgt_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_lf_upr_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_bty_stop_up_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_floor_contact_v1/2kfa_nc16
/shots/sp2/op04/pix/ptex/op04_env
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_bty_key_only_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_rkey_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_rfl_lf_lwr_v1/tvfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_out_floor_bty_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_rt_lwr_v1/2kfa_nc16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_rfl_rt_upr_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_redwire_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rtex/op04_lgts_mstokes_tnt_shd_lf_lwr_rim_v7
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_spine_led_bty_v1/2kfa_lg16
/shots/sp2/op04/pix//omf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_depth_v1/tvfa_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_rkey_alt_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_floor_key_cast_shadows_v1/2kfa_lny16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_warm_upr_back_v1/256sq_ncf
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_tnt_beam_occ_amb_sd_envdir_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_rkey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_rt_lwr_v1/tvfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_occ_amb_sd_envdir_v1/2kfa_nc16
/shots/sp2/op04/pix/ptex/op04_env/generic/v1/ln32_tif
/shots/sp2/op04/pix/pnt/op04_floorcloth_rototest_v2/tvfa_lg10
/shots/sp2/op04/comp//jschmidt
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/ptex/op04_env/generic/v2
/shots/sp2/op04/pix/mattes/op04_ock_mtt_v2
/shots/sp2/op04/pix/mattes/op04_floorcloth_matte_v2
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_scr_sidefill_v1
/shots/sp2/op04/pix/mattes/op04_ock_mtt_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_bty_v1
/shots/sp2/op04/pix/ref/op04_cut_ref_v1
/shots/sp2/op04/pix/pnt/op04_bg2_pnt_v2/tvfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_floor_contact_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_depth_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_nokey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_cam_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_spine_led_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_depth_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_rt_lwr_sd_envdir_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_led_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/out/op04_comp_v18/2kfa_lg10
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_rt_lwr_sd_envdir_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_cam_bty_v1
/shots/sp2/op04/pix/ref/op04_anim_ref_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_contact_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_bty_stop_up_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_lf_lwr_sd_envdir_v1/2kfa_nc16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_rfl_rt_lwr_v1/2kfa_nc16
/shots/sp2/op04/pix//pvr
/shots/sp2/op04/pix//ptex
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_front_fill_v1/2ksq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_rfl_rt_lwr_v1
/shots/sp2/op04/pix/pnt/op04_floorcloth2_rototest_v1/tvfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_occ_amb_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_depth_v1/tvfa_ncf
/shots/sp2/op04/pix/rtex/op04_lgts_mstokes_tnt_shd_lf_lwr_rim_v7/256sq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_bty_v1/2kfa_lg16
/shots/sp2/op04/comp//eddie
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_rkey_v1/2ksq_ncf
/shots/sp2/op04/pix/mattes/op04_ock_mtt_v1/2kfa_lg8
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_occ_amb_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_rt_upr_v1/2kfa_nc16
/shots/sp2/op04/pix/pnt/op04_bg2_pnt_v2
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_rfl_rt_upr_v1/2kfa_nc16
/shots/sp2/op04/pix/pnt/op04_floorcloth_rototest_v2
/shots/sp2/op04/pix/pnt/op04_floorcloth_rototest_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_rkey_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_rkey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/ptex/op04_env/generic
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_lscr_fill_v2
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_lscr_fill_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_spcl_lgt_cam_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_rt_upr_sd_envdir_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_nokey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_out_floor_bty_v1/tvfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_rkey_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_mm_axis_v1/tvfa_lny16
/shots/sp2/op04/pix/raw/op04_bg_v2/tvfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_led_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_floor_contact_v1/tvfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_lf_lwr_v1/2kfa_nc16
/shots/sp2/op04/pix/out/op04_mstokes_comp_bg_v1/tvfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_redwire_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_alt_rkey_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_alt_rkey_v1/256sq_ncf
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_warm_upr_back_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_spine_led_bty_v1
/shots/sp2/op04/pix/maya/op04_jschmidt_tiletest_dx_v2/tvfa_bi8
/shots/sp2/op04/pix/avi/from_vfo
/shots/sp2/op04/pix//mov
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_bty_stop_up_v1/tvfa_lg16
/shots/sp2/op04/pix/mattes/op04_floorwood_matte_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_key_cast_shadows_v1
/shots/sp2/op04/pix/ref/op04_op04_fisheye_ref_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_spine_led_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_rkey_alt_bty_v2/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_spine_led_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_lf_upr_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_rfl_rt_lwr_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_hinge_bty_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_rt_upr_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_nokey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_lf_lwr_sd_envdir_v1/2kfa_nc16
/shots/sp2/op04/pix//tile
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_tnt_beam_occ_amb_sd_envdir_v1/2kfa_nc16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_rfl_rt_upr_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_floorbounce_v1/2ksq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_rkey_alt_bty_v2
/shots/sp2/op04/pix/out/op04_comp_v18
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_rkey_alt_bty_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_warm_upr_back_v1/2ksq_ncf
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_skylight_v1/256sq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_lf_upr_sd_envdir_v1/2kfa_nc16
/shots/sp2/op04/pix/plates/op04_bg_v2/tvfa_lg10
/shots/sp2/op04/comp//jhillin
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_contact_v1/tvfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_rt_upr_v1/tvfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_lf_lwr_sd_envdir_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_girder_key_cast_shadows_v1
/shots/sp2/op04/comp//mcarter
/shots/sp2/op04/pix/maya/op04_lgrane_anim_render_v82/tvfa_bi8
/shots/sp2/op04/pix/m2v/dykstra_dvd
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_rfl_rt_upr_v1/tvfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_led_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_tnt_beam_occ_amb_v1/2kfa_nc16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_scr_sidefill_v1/256sq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_rkey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_floorbounce_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_bty_v1/tvfa_lny16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_scr_sidefill_v1/2ksq_ncf
/shots/sp2/op04/comp//chikako
/shots/sp2/op04/pix/pnt/op04_floorcloth2_rototest_v1
/shots/sp2/op04/pix/rtex/op04_lgts_mstokes_tnt_shd_lf_lwr_rim_v7/1ksq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_bty_v2/tvfa_lny16
/shots/sp2/op04/pix/maya/op04_jschmidt_tiletest_dx_v2
/shots/sp2/op04/pix/out/op04_mstokes_comp_bg_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_spcl_lgt_cam_bty_v1
/shots/sp2/op04/pix/ref/op04_guide_ref_v1/tvfa_bi8
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_floor_contact_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_cam_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/pnt/op04_ock_comp_test_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_led_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_girder_key_cast_shadows_v1/2kfa_lny16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_rt_upr_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_depth_v1/2kfa_ncf
/shots/sp2/op04/pix//out
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_rkey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_rkey_alt_bty_v2/tvfa_lg16
/shots/sp2/op04/pix/raw/op04_bg_v2
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_bty_key_only_v1
/shots/sp2/op04/pix/mattes/op04_floorwood_matte_v1/tvfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_contact_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_skylight_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_floorbounce_v1/256sq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_key_cast_shadows_v1/2kfa_lny16
/shots/sp2/op04/pix/out/op04_comp_v20/2kfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_floor_contact_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_bty_stop_up_v1/2kfa_lg16
/shots/sp2/op04/pix/ptex/op04_env/generic/v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_rkey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_rkey_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_bty_v1/2kfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_rfl_lf_upr_v1
/shots/sp2/op04/pix/mattes/op04_animpull_v1/tvfa_bi8
/shots/sp2/op04/pix/ref/op04_guide_ref_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_hinge_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_bty_key_only_v1/2kfa_lg16
/shots/sp2/op04/pix/pnt/op04_floorwood_rototest_v1/2kfa_lg10
/shots/sp2/op04/pix/ref/op04_op04_fisheye_ref_v1/misc_bi8
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_front_fill_v1/256sq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_mm_axis_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_bty_stop_up_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_led_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_floor_key_cast_shadows_v1
/shots/sp2/op04/pix/pnt/op04_floorcloth_rototest_v1/2kfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_rkey_alt_bty_v2/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_led_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_nokey_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_girder_key_cast_shadows_v1/tvfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_rfl_lf_upr_v1/tvfa_nc16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_rt_lwr_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_cam_bty_v1
/shots/sp2/op04/pix/pnt/op04_floorcloth_rototest_v2/2kfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_spine_led_bty_v1
/shots/sp2/op04/comp//mstokes
/shots/sp2/op04/pix//ref
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_front_fill_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_depth_v1/tvfa_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_depth_v1/2kfa_ncf
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_rfl_lf_lwr_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_occ_amb_v1/tvfa_nc16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_rfl_lf_upr_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_spine_led_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_rfl_rt_lwr_v1/tvfa_nc16
/shots/sp2/op04/pix/mattes/op04_animpull_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_girder_skylight_cast_shadows_v1/2kfa_lny16
/shots/sp2/op04/pix//swatch
/shots/sp2/op04/pix//inferno
/shots/sp2/op04/pix/out/op04_comp_v19
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_bty_stop_up_v1/2kfa_lg16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_lf_upr_sd_envdir_v1/2kfa_nc16
/shots/sp2/op04/pix//rnd
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_floor_contact_v1/tvfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_floor_skylight_cast_shadows_v1/tvfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_cam_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/out/op04_comp_v18/tvfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_spcl_lgt_only_cam_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/ref/op04_cut_ref_v1/tvfa_bi8
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_floor_key_cast_shadows_v1/tvfa_lny16
/shots/sp2/op04/pix//mattes
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_depth_v1/2kfa_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_led_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_bty_stop_up_v1
/shots/sp2/op04/pix/mattes/op04_ock_mtt_v1/tvfa_lg8
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_bty_key_only_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_rkey_bty_v1
/shots/sp2/op04/pix/mov/dykstra_dvd
/shots/sp2/op04/pix/out/op04_comp_v19/tvfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_floor_skylight_cast_shadows_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_lf_lwr_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_alt_rkey_v1/2ksq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_bty_v2
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_nokey_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_spine_led_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/mattes/op04_floorcloth2_matte_v1/tvfa_lg10
/shots/sp2/op04/pix/out/video
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_lscr_fill_v1/2ksq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_rkey_alt_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_led_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_key_cast_shadows_v1/tvfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_bty_key_only_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_rt_upr_sd_envdir_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_led_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_cam_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_redwire_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_cam_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/pnt/op04_floorwood_rototest_v1/tvfa_lg10
/shots/sp2/op04/pix//raw
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_rt_lwr_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_rkey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_rfl_lf_upr_v1
/shots/sp2/op04/pix/out/op04_comp_v20
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_floor_contact_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_depth_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_led_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_bty_stop_up_v1/tvfa_lg16
/shots/sp2/op04/pix/raw/op04_bg_v2/2kfa_lg10
/shots/sp2/op04/pix/plates/op04_bg_v2
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_lf_lwr_v1/tvfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_spine_led_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_tnt_beam_occ_amb_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_depth_v1/tvfa_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_girder_skylight_cast_shadows_v1/tvfa_lny16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_lscr_fill_v2/256sq_ncf
/shots/sp2/op04/pix/maya/op04_lgrane_anim_render_v90
/shots/sp2/op04/pix/swatch/op04_lgts_tnt_swatch_v1
/shots/sp2/op04/pix/out/op04_lt_comp_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_rt_lwr_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_rkey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/pnt/op04_ock_comp_test_v1/2kfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_rkey_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_nokey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_rkey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/ptex/op04_env/generic/v2/ln32_tif
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_rfl_lf_upr_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_girder_skylight_cast_shadows_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_rkey_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_cam_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/out/op04_lt_comp_v1/2kfa_lg10
/shots/sp2/op04/pix/mattes/op04_ock_mtt_v2/2kfa_lg8
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_shad_lscr_fill_v1/256sq_ncf
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_nokey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_rfl_rt_lwr_v1
/shots/sp2/op04/pix/out/op04_lt_comp_v1/tvfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_out_floor_bty_v1/2kfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_dclaw_led_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_floor_contact_v1/tvfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_dclaw_rkey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_mm_axis_v1/2kfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_bty_stop_up_v1
/shots/sp2/op04/pix/maya/op04_lgrane_anim_render_v90/tvfa_bi8
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_lf_upr_v1
/shots/sp2/op04/pix/maya/op04_jschmidt_tiletest_v2/tvfa_bi8
/shots/sp2/op04/pix/ptex/op04_env/generic/v1/ln32_tx
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_lf_lwr_v1/2kfa_nc16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_occ_amb_sd_envdir_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/ptex/op04_env/generic/v2/ln32_tx
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_spine_led_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_rfl_rt_upr_v1
/shots/sp2/op04/pix/swatch/op04_lgts_tnt_swatch_v2
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_lf_upr_v1/tvfa_nc16
/shots/sp2/op04/pix/pnt/op04_floorcloth_rototest_v1/tvfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_nokey_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/mattes/op04_floorcloth_matte_v2/tvfa_lg10
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_rkey_alt_bty_v2
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_rkey_alt_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_bty_key_only_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_beam_bty_v2/2kfa_lny16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_bty_key_only_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_rt_upr_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_dclaw_spcl_lgt_only_cam_bty_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_bty_key_only_v1
/shots/sp2/op04/pix/maya/op04_jschmidt_tiletest_v2
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_lwr_spine_led_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_bty_key_only_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_bty_key_only_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_lf_lwr_sd_envdir_v1
/shots/sp2/op04/pix//plates
/shots/sp2/op04/pix/pnt/op04_floorwood_rototest_v1
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_lf_lwr_v1
/shots/sp2/op04/pix//avi
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_rkey_bty_v1/2kfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_occ_amb_lf_upr_sd_envdir_v1
/shots/sp2/op04/comp//alex
/shots/sp2/op04/pix/rtex/op04_lgts_tnt_occ_amb_rt_lwr_sd_envdir_v1
/shots/sp2/op04/pix/mattes/op04_floorwood_matte_v1/2kfa_lg10
/shots/sp2/op04/pix/swatch/op04_lgts_mstokes_swatch_v2
/shots/sp2/op04/pix/out/op04_comp_v19/2kfa_lg10
/shots/sp2/op04/pix/pnt/op04_floorcloth2_rototest_v1/2kfa_lg10
/shots/sp2/op04/pix//rtex
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_lwr_floor_contact_v1
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_lf_upr_dclaw_cam_bty_v1/tvfa_lg16
/shots/sp2/op04/pix/rnd/op04_lgts_tnt_tnt_rt_upr_bty_v1
                                                                                                                                                                                                                                                                                                                                           prodlist.txt                                                                                        0100666 0021522 0000024 00000005756 10037545535 012671  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   anim.maya
cam_main.pit
cam_main.sprib
def_check.lgts
def_check.mtl
def_check.rhdr
def_check.sprib
doc.pit
doc.sprib
lgts_rshrider.lgts
lgts_rshrider.mtl
lgts_rshrider.rhdr
lgts_rshrider.sprib
lgts_tnt.lgts
lgts_tnt.mtl
lgts_tnt.rhdr
lgts_tnt.sprib
mm.maya
mm_all.pit
mm_all.sprib
mm_clean.maya
out_comp_bg.pix
plates_bg.pix
prop_master.pit
prop_master.sprib
raw_bg.pix
rnd_def_check_bty.pix
rnd_lgts_tnt_occ_amb_tnt_bty.pix
rnd_lgts_tnt_occ_amb_tnt_bty_sd_envdir.pix
rnd_lgts_tnt_occ_rfl_tnt_bty.pix
rnd_lgts_tnt_shadmat_doc_face_fill.pix
rnd_lgts_tnt_shadmat_doc_front_soft_fill.pix
rnd_lgts_tnt_shadmat_doc_key.pix
rnd_lgts_tnt_shadmat_doc_lamp_fill.pix
rnd_lgts_tnt_shadmat_doc_lf_key.pix
rnd_lgts_tnt_shadmat_doc_skylight_fill.pix
rnd_lgts_tnt_shadmat_doc_warm_upr_back.pix
rnd_lgts_tnt_shadmat_tnt_lf_lwr.pix
rnd_lgts_tnt_shadmat_tnt_welding_rig.pix
rnd_lgts_tnt_tnt_box2_lid_axis.pix
rnd_lgts_tnt_tnt_bty.pix
rnd_lgts_tnt_tnt_bty_stop_down.pix
rnd_lgts_tnt_tnt_cigar_bty.pix
rnd_lgts_tnt_tnt_lf_lwr_bty.pix
rnd_lgts_tnt_tnt_lf_lwr_contact.pix
rnd_lgts_tnt_tnt_lf_lwr_dclaw_led_bty.pix
rnd_lgts_tnt_tnt_lf_lwr_nodoc_bty.pix
rnd_lgts_tnt_tnt_lf_lwr_nowarmuprback_bty.pix
rnd_lgts_tnt_tnt_lf_lwr_spine_led_bty.pix
rnd_lgts_tnt_tnt_lf_lwr_stop_up_bty.pix
rnd_lgts_tnt_tnt_lf_lwr_tnt_welding_bty.pix
rnd_lgts_tnt_tnt_lf_upr_bty.pix
rnd_lgts_tnt_tnt_lf_upr_dclaw_led_bty.pix
rnd_lgts_tnt_tnt_lf_upr_nodoc_bty.pix
rnd_lgts_tnt_tnt_lf_upr_nowarmuprback_bty.pix
rnd_lgts_tnt_tnt_lf_upr_pipegrab_bty.pix
rnd_lgts_tnt_tnt_lf_upr_spine_led_bty.pix
rnd_lgts_tnt_tnt_lf_upr_stop_up_bty.pix
rnd_lgts_tnt_tnt_lf_upr_tnt_welding_bty.pix
rnd_lgts_tnt_tnt_match_bty.pix
rnd_lgts_tnt_tnt_mm_axis.pix
rnd_lgts_tnt_tnt_rt_lwr_bty.pix
rnd_lgts_tnt_tnt_rt_lwr_dclaw_led_bty.pix
rnd_lgts_tnt_tnt_rt_lwr_spine_led_bty.pix
rnd_lgts_tnt_tnt_rt_lwr_stop_up_bty.pix
rnd_lgts_tnt_tnt_rt_lwr_welding_bty.pix
rnd_lgts_tnt_tnt_rt_upr_bty.pix
rnd_lgts_tnt_tnt_rt_upr_dclaw_led_bty.pix
rnd_lgts_tnt_tnt_rt_upr_pipegrab_bty.pix
rnd_lgts_tnt_tnt_rt_upr_spine_led_bty.pix
rnd_lgts_tnt_tnt_rt_upr_stop_up_bty.pix
rnd_lgts_tnt_tnt_rt_upr_tnt_welding_bty.pix
rnd_lgts_tnt_tnt_welding_crate_axis.pix
rnd_lgts_tnt_tnt_welding_rig.pix
tex_env_generic.tex
tex_lgts_tnt_occ_amb_tnt_bty.tex
tex_lgts_tnt_occ_amb_tnt_bty_sd_envdir.tex
tex_lgts_tnt_occ_rfl_tnt_bty.tex
tex_lgts_tnt_shad_lgt_doc_key.depth
tex_lgts_tnt_shad_lgt_doc_lf_key.depth
tex_lgts_tnt_shad_lgt_face_fill.depth
tex_lgts_tnt_shad_lgt_front_soft_fill.depth
tex_lgts_tnt_shad_lgt_lamp_fill.depth
tex_lgts_tnt_shad_lgt_skylight_fill.depth
tex_lgts_tnt_shad_lgt_warm_upr_back.depth
tex_lgts_tnt_shad_tnt_all_tnt_welding_bty.depth
tex_lgts_tnt_shad_tnt_lf_lwr.depth
tex_lgts_tnt_shad_tnt_rt_lwr_welding_bty.depth
tex_lgts_tnt_shad_tnt_welding_rig.depth
tnt_lf_lwr.pit
tnt_lf_lwr.sprib
tnt_lf_upr.pit
tnt_lf_upr.sprib
tnt_lo_lf_lwr.pit
tnt_lo_lf_lwr.sprib
tnt_lo_lf_upr.pit
tnt_lo_lf_upr.sprib
tnt_lo_rt_lwr.pit
tnt_lo_rt_lwr.sprib
tnt_lo_rt_upr.pit
tnt_lo_rt_upr.sprib
tnt_rt_lwr.pit
tnt_rt_lwr.sprib
tnt_rt_upr.pit
tnt_rt_upr.sprib
                  foo.0001.rla                                                                                        0100666 0021522 0000024 00000000015 10045004653 012077  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   foo.0001.rla
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   foo.0002.rla                                                                                        0100666 0021522 0000024 00000000015 10045004723 012076  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   foo.0002.rla
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   foo.0003.rla                                                                                        0100666 0021522 0000024 00000000015 10045004731 012076  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   foo.0003.rla
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   foo.0004.rla                                                                                        0100666 0021522 0000024 00000000015 10045004740 012077  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   foo.0004.rla
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   foo.0005.rla                                                                                        0100666 0021522 0000024 00000000015 10045004750 012101  0                                                                                                    ustar   jhillin                         user                                                                                                                                                                                                                   foo.0005.rla
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   