from netaddr import IPNetwork

subnet = raw_input("Please enter target subnet: ")

for ip in IPNetwork(subnet).iter_hosts():
    #print '%s' % ip
    target = "http://" + ip + "/script"
    try:
        response = urllib2.urlopen(target)
        print
    except urllib2.HTTP.Error, e:
        return