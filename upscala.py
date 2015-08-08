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

for root, dirs, files in os.walk("/Users/ciaranfitzpatrick/Documents"):
	for file in files:
		if file.endswith(".scala"):
			grepForBug(file)
		else:
			print "No scala files found in folder..."
