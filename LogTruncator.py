#Given the percent of people playing R, P, or S generate a simulated bracket
#Expand into being a MTG Metagame simulator?
#IDs seems hard to simulate.
#Given 2 dates, make a new file with the same name as the original, but with (DATESTART-DATEEND) postpended to the file name
import re
import sys, getopt, shutil

"""
Features/flags to consider for future additions:
Done	-f <fileName>: Marks single file to operate on
Done	-s <timestamp>: Truncate all lines prior to this
		-o Overwrite file

"""
def main(argv):

	try:
		opts, args = getopt.getopt(argv, "e:s:f:v", ["OVERWRITE", "VERBOSE"])
	except getopt.GetoptError:
		invalid_args()

	#Files and file names
	fileName, f, tempFile = "", "", ""
	tempName = ""

	#Flags
	replace, forceOverwrite, verbose = False, False, False

	#Timestamps like this: 2016-03-14 16:34:55
	start, end = "0", "9"

	for opt, arg in opts:
		if opt == "-h":
			show_usage()
		elif opt == "-f":
			fileName = arg
		elif opt == "-s":
			start = arg
		elif opt == "-e":
			end = arg
		elif opt in ["-v", "--VERBOSE"]:
			verbose = True
		else:
			invalid_args()

	with open(fileName, 'r') as f:
		tempName = "({0}-{1})".format(start, end).replace(" ", "_") + fileName
		tempName = "truncated.log"
		tempFile = open(tempName, 'w')
		doWrite = False

		regexp = re.compile('^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}') #Regex for date
		for line in f:
			words = line.split(" ")
			if len(words) > 2:
				time = words [0] + " " + words[1]
				if regexp.match(time):		
					if start < time and not doWrite:
						print "Starting writing at {}".format(time)
						doWrite = True
					elif end < time:
						print "Time span ended at {}".format(time)
						break
			if doWrite:
				tempFile.write(line)
		print "Closing file"
		tempFile.close()

def show_usage():
	print "Usage: LogTruncator.py -f <File to check> -s <Start Time> -e <End time>"
	print "\t-f flags for the input file"
	print "\tTimestamps formatted like: \"2016-03-14 16:34:55\""
	# print "\t--OVERWRITE flags to automatically overwrite the source file with the replaced text"
	sys.exit(2)

def invalid_args():
	print "\nInvalid arguments."
	show_usage()

if __name__ == "__main__":
	if len(sys.argv) <= 1:
		show_usage()
	else:
		main(sys.argv[1:])