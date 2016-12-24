"""
Generates names like Andreessen Horowitz as a16z

Usage: python numify_names.py Andreessen Horowitz
Returns: Numified: a16z
"""

from sys import argv, exit

if len(argv) < 2:
	print "Usage: python %s name" % argv[0]
	exit(2)

names = ''.join(argv[1:]).lower()
numified = "%s%d%s" % (names[0], len(names) - 2, names[-1]) 
print "Numified: %s" % numified