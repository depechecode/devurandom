from netaddr import *
import urllib2

def ssiReferer(ip):
	request = urllib2.Request("http://"+ ip, headers={"Referer" : "<!--#echo var='DATE_LOCAL' -->"})
	contents = urllib2.urlopen(request).read()
	if "time" in contents:
		print "Check this one out, looks dodgy!"
	else:
		print "Nothing on " + ip
	return


def ssiAgent(ip):
	request = urllib2.Request("http://"+ ip, headers={"User-Agent" : "<!--#echo var='DATE_LOCAL' -->"})
	contents = urllib2.urlopen(request).read()
	if "time" in contents:
		print "Check this one out, looks dodgy!"
	else:
		print "Nothing on " + ip
	return


source = raw_input("Please enter a subnet to scan for ssi header issues: ")
ips = IPNetwork(source)

for ip in ips:
	ssiReferer(ip)
	ssiAgent(ip)