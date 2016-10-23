import re
import operator
import sys, getopt, shutil

"""
TODO: Make a method to increment an ASCII string
TODO: Use that method to read from a file and write it back
"""

#Counts and stacks output lines from logs
def main(argv):



def show_usage():
	print "Usage: LogStacker.py -f <File to check> -l <int 1-7> -u"
	print "\t-f flags for the input file"
	print "\t-f max level of logs to include"
	print "\t-u to treat all UUIDs the same"
	sys.exit(2)

def invalid_args():
	print "\nInvalid arguments."
	show_usage()

def extract_message(line):
	#Remove the timestamp
	return line[24:-1]

if __name__ == "__main__":
	if len(sys.argv) <= 1:
		show_usage()
	else:
		main(sys.argv[1:])