from netaddr import IPNetwork

subnet = raw_input("Please enter target subnet: ")

for ip in IPNetwork(subnet).iter_hosts():
	print "http://" + "%s" % ip
    #target = "http://" + ip + "/script"
    