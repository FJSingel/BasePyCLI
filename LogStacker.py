import re
import operator
import sys, getopt, shutil

"""
TODO: Add filtering by message occurrance
TODO: Replace UUIDs with wildcard chars to increase stacking
"""

#Counts and stacks output lines from logs
def main(argv):

	try:
		opts, args = getopt.getopt(argv, "f:l:u")
	except getopt.GetoptError:
		invalid_args()

	#Files and file names

	fileName, f = "", ""
	verbose = False
	replaceUUIDs = False
	LOG_LEVELS = ["OFF", "FATAL", "ERROR", "WARN", "INFO", "DEBUG", "TRACE"]

	#Flags
	for opt, arg in opts:
		if opt == "-f":
			fileName = arg
		elif (opt == "-l" and 1 <= int(arg) <= 7):
			LOG_LEVELS = LOG_LEVELS[:int(arg)]
		elif opt == "-u":
			replaceUUIDs = True;
		else:
			invalid_args()

	with open(fileName, 'r') as f:
		"""
		Strip timestamp
		add to dict (increment count)
		Display counts
		"""
		errorCounts = {}
		timeStampRegex = re.compile('^\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d,\d\d\d ')
		
		for line in f:
			if timeStampRegex.search(line) is not None:
				message = extract_message(line)
				if replaceUUIDs:
					message = re.sub("[0-9a-f]{8}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{12}","XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", message)
				if (message.split(" ", 1)[0] in LOG_LEVELS):
					try:
						errorCounts[message] += 1
					except KeyError:
						errorCounts[message] = 1

		entries_sorted_by_occurrances = sorted(errorCounts.items(), key=operator.itemgetter(0))
		for msg, qty in entries_sorted_by_occurrances:
			print "{0}x {1}".format(qty, msg)


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