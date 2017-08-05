from collections import Counter
import sys, getopt, shutil

"""
TODO: Add Frequency Table
TODO: Add Dict?
TODO: Solve by Frequency Analysis
"""

#Counts and stacks output lines from logs
def main(argv):

	fileName = argv[0]
	totalCount = Counter()

	#Counts all the chars
	with open(fileName, 'r') as f:
		for line in f:
			totalCount += Counter(line.lower());
	print totalCount

def show_usage():
	print "Usage: CipherSolver.py <File to solve>"
	sys.exit(2)

def invalid_args():
	print "\nInvalid arguments."
	show_usage()


if __name__ == "__main__":
	if len(sys.argv) <= 1:
		show_usage()
	else:
		main(sys.argv[1:])