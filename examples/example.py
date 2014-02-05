# pkg.mod
# Basic example demonstrating usage of the interface
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Tue Jul 09 14:20:34 2013 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: example.py [] benjamin@bengfort.com $

"""
Basic example demonstrating usage of the interface
"""

##########################################################################
## Imports
##########################################################################

from BerkeleyInterface import *

# This should be the path to the Berkeley Parser jar file
cp = r'C:\berkeleyparser\BerkeleyParser-1.7.jar'

# Always start the JVM first!
startup(cp)

# Set input arguments
# See the BerkeleyParser documentation for information on arguments
# Notably: a grammar file ("gr") is required, and if inputFile / outputFile
# are not given, it will default to stdin/stdout
gr = r'C:\berkeleyparser\eng_sm6.gr'
args = {"gr":gr, "tokenize":True, "inputFile":"testinput.txt"}

# Convert args from a dict to the appropriate Java class
opts = getOpts(dictToArgs(args))

# Load the grammar file and initialize the parser with our options
parser = loadGrammar(opts)

# Now, actually parse the input file
# (Since we didn't specify an output file, it will go to stdout)
parseInput(parser, opts)

# At this point, we have done the equivalent of running from the command line:
# java -client -jar C:\berkeleyparser\BerkeleyParser-1.7.jar\BerkeleyParser-1.7.jar -gr eng_sm6.gr -inputFile testinput.txt -tokenize

# We can change opts between parses, in this case to change input/outputs
# See documentation for getOpts for a list of options which are safe to modify
# and will not require reinitializing the parser
opts.inputFile = "testinput2.txt"
opts.outputFile = opts.inputFile + ".parsed"

# Or, we could modify the original args dictionary:
args["inputFile"] = "testinput2.txt"
args["outputFile"] = args["inputFile"] + ".parsed"
opts = getOpts(dictToArgs(args))

# Parse again, with our modified options
parseInput(parser, opts)

# We can also take advantage of Python's built-in StringIO class,
# which allows us to use strings like files
from StringIO import StringIO
strIn = StringIO("Hello, world!\nThe quick brown fox jumped over the lazy dogs.")
strOut = StringIO()
parseInput(parser, opts, outputFile=strOut)

# Now we can retrieve the output as a string:
result = strOut.getvalue()
print "\nStringIO Result:\n",result

# That's all, folks!
shutdown()
