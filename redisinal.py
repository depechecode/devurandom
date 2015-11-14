# Import socket module
# -*- coding: utf-8 -*-
import socket
from netaddr import IPNetwork           

# Define the port on which you want to connect
port = 6379                

def connectRedis (ip):
	# connect to the server on local computer
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
	s.connect((str(ip), port))

	# receive data from the server
	s.send ("CONFIG GET *" + "\n")
	print s.recv(1024)
	# close the connection
	s.close()

def subnetSearch(subnet):
	for ip in IPNetwork(subnet).iter_hosts():
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
		result = sock.connect_ex((str(ip),6379))
		if result == 0:
			print "Port is open on %s" % str(ip)
   			print ""
   			print "Connecting to Redis: "
   			print ""
   			connectRedis(ip)
   		else:
   			print "Port is not open %s" % str(ip)

def banner():
    print """
.______       _______  _______   __       _______. __  .__   __.      ___       __      
|   _  \     |   ____||       \ |  |     /       ||  | |  \ |  |     /   \     |  |     
|  |_)  |    |  |__   |  .--.  ||  |    |   (----`|  | |   \|  |    /  ^  \    |  |     
|      /     |   __|  |  |  |  ||  |     \   \    |  | |  . `  |   /  /_\  \   |  |     
|  |\  \----.|  |____ |  '--'  ||  | .----)   |   |  | |  |\   |  /  _____  \  |  `----.
| _| `._____||_______||_______/ |__| |_______/    |__| |__| \__| /__/     \__\ |_______|
                                                                                        
                           Redis Lack of Authentication Checker (python redisinal.py)"""

if __name__ == "__main__":
   banner()
   subnet = raw_input("Please enter target subnet: ")
   subnetSearch(subnet)
