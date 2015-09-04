import urllib2
from netaddr import IPNetwork

subnet = raw_input("Please enter target subnet: ")

for ip in IPNetwork(subnet).iter_hosts():
    #print '%s' % ip
    #target = "http://" + ip + "/script"
    target = "http://" + str(ip) + "/"
    print "Trying " + target
    try:
        response = urllib2.urlopen(target)
        print response
    except urllib2.HTTP.Error, e:
        print "No Server Found at " + target