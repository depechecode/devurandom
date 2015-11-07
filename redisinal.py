import socket
import telnetlib
from netaddr import IPNetwork

subnet = raw_input("Please enter target subnet: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for ip in IPNetwork(subnet).iter_hosts():
	result = sock.connect_ex((str(ip),6379))
	if result == 0:
   		print "Port is open on %s" % str(ip)
   		print ""
   		print "Connecting to Redis: "
   		tn = telnetlib.Telnet(ip)
   		tn.write("CONFIG GET *"+"\n")
   		output = tn.read_all()
   		if "dbfilename" in output:
   			print "Looks like you can manipulate the CONFIG.."
   		else:
   			print "Not sure this redis is vulnerable.."
	else:
   		print "Port is not open %s" % str(ip)








