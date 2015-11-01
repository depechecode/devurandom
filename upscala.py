import os

def grepForBug(file):
	print file
	txt = open(file, 'r')
	for line in txt:
		if("Query") in line and " + " in line:
			print "Possible Dynamic SQL Statement Found"
			print line
		elif("sys.process") in line:
			print "Review file for OS Interaction"
			print line
		elif("XMLDecoder(") in line:
			print "Review file XXE Issues"
			print line
		else:
			print "."

for root, dirs, files in os.walk("/Users/Documents"):
	for file in files:
		if file.endswith(".java"):
			grepForBug(file)
		else:
			print "No java files found in folder..."
