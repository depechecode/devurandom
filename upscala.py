import os

def sqlInj(file):
	print file
	txt = open(file, 'r')
	for line in txt:
		if("Query") in line and " + " in line:
			print "Possible Dynamic SQL Statement Found"
			print line
		else:
			print "."

def comExec(file):
	print file
	txt = open(file, 'r')
	for line in txt:
		if ("sys.process") in line:
			print "Review file for OS Interaction"
			print line
		else:
			print "."

for root, dirs, files in os.walk("/Users/Documents"):
	for file in files:
		if file.endswith(".scala"):
			sqlInj(file)
			comExec(file)
