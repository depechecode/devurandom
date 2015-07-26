import os
#txt = open('file.php', 'r')

def phpFind(file):
	print file
	txt = open(file, 'r')
	for line in txt:
		if("eval" or "exec" or "passthru") in line and "$_" in line:
		#if "eval" in line or "exec" in line and "$_" in line:
			print "...Code Exec Found!?"
			print line
		else:
			print "."

def javaFind(file):
	print file
	txt = open(file, 'r')
	for line in txt:
		if (".exec" or "system(") in line:
			print "...Code Exec Found!?"
			print line
		else:
			print "."

for root, dirs, files in os.walk("/Users/Documents"):
	for file in files:
		if file.endswith(".php"):
			phpFind(file)
		elif file.endswith(".java"):
			javaFind(file)