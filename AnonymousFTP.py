#=========================================================#
# [+] Title: FTP Anonymous Login Scanner	          #
# [+] Script: AnonFTP.py     				  #
# [+] Rob Fitzpatrick		                          #
#=========================================================#

import ftplib,sys,socket

#Define Anon Login Function
def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login("anonymous", "me@your.com")
        print "\n[+]" + str(hostname) + " FTP Anonymous Logon Succeded"
        ftp.quit()
        return True
    except Exception, e:
        print "\n[-] %s FTP Logon Failed." % str(hostname)
        return False
#Take in first 3 octets of /24 range as argument
addr_range = sys.argv[1]+".%d"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Cycle through /24 attempting anon ftp login
for i in range(1, 254):
	ip = addr_range % i
	anonLogin(ip)
