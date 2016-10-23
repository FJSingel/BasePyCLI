import re
import sys, getopt, shutil

"""
Features/flags to consider for future additions:
Done	-f <fileName>: Marks single file to operate on
		-d <dirName>: Marks a directory to recursively operate on
		-x <fileExt>+: List of file extensions to accept
Done	-R: Flag to automatically remove whitespace.
	 	-V, --Verbose: Verbose flag
"""
def main(argv):

	try:
		opts, args = getopt.getopt(argv, "hR:f:v", ["OVERWRITE", "VERBOSE"])
	except getopt.GetoptError:
		invalid_args()

	#Files and file names
	fileName, f, tempFile = "", "", ""
	tempName = "tempFile.txt"

	#Flags
	replace, forceOverwrite, verbose = False, False, False

	for opt, arg in opts:
		if opt == "-h":
			show_usage()
		elif opt == "-R":
			replace = True
			if arg != "":
				tempName = arg
		elif opt == "-f":
			fileName = arg
		elif opt == "--OVERWRITE":
			replace = True
			forceOverwrite = True
		elif opt in ["-v", "--VERBOSE"]:
			verbose = True
		else:
			invalid_args()

	#Don't let the input file be the temp file too. You'll just erase the file.
	if fileName == tempName:
		raise ValueError("The input and output files must have different names")

	with open(fileName, 'r') as f:
		if replace:
			tempFile = open(tempName, 'w')

		tabLines = []
		spaceLines = []
		lineNO = 1
		regexp = re.compile('[ ]+$') #Regex for spaces at end of line
		for line in f:
			if "\t" in line:
				tabLines.append(lineNO)
			if regexp.search(line) is not None:
				spaceLines.append(lineNO)
			if replace:
				cleanedLine = line.replace("\t", "    ").rstrip()
				tempFile.write(cleanedLine + "\n")
			lineNO += 1

		if verbose or not replace:
			print "\nLines with extra Spaces: ", spaceLines
			print "Number of Space Lines: ", len(spaceLines)

			print "\nLines with tabs:", tabLines
			print "Number of Tab Lines", len(tabLines)

		if replace:
			tempFile.close()
			if not forceOverwrite:
				overwrite = raw_input("\nOutput written to {0}. Replace original file with contents of {0}? (Y/N)\n".format(tempName))
				if overwrite.upper() == 'Y':
					forceOverwrite = True
			
			if forceOverwrite:
				shutil.copy(tempName, fileName)
				if verbose:
					print "Source file overwritten. Whitespace removed."
			elif verbose:
				print "{0} left for review.".format(tempName)

def show_usage():
	print "Usage: WhiteSpaceFinder.py -f <File to check> [-R <name of output file>] [--OVERWRITE] [--VERBOSE]"
	print "\t-f flags for the input file"
	print "\t-R flags to replace whitespace. The filename associated is where output is written to."
	print "\t--OVERWRITE flags to automatically overwrite the source file with the replaced text"
	sys.exit(2)

def invalid_args():
	print "\nInvalid arguments."
	show_usage()

if __name__ == "__main__":
	if len(sys.argv) <= 1:
		show_usage()
	else:
		main(sys.argv[1:])