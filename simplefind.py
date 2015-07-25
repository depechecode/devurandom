import os
#txt = open('file.php', 'r')

for root, dirs, files in os.walk("/Users/Documents"):
	for file in files:
		if file.endswith(".php"):
			print file
			txt = open(file, 'r')
			for line in txt:
				if "eval" in line and "$_" in line:
					print "Code Exec Found?"
					print line
				else:
					print "Nothing!"