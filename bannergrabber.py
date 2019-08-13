#Banner Grabber

#Write a tool that attempts to connect to four different ports (21,23,25,80)
#on a range of IP address (10.28.5.0/24).  Use the socket module to attempt
#the connections.  If a connection is successful, print to the screen the name
#of the host and IP address.  If it is unsuccessful, print to the screen a
#message that indicates failure.


import socket

def main():
   ports = [21,23,25,80]
   ips = "192.168.195."
   for octet in range(0,254):
       for port in ports:
           ip = ips + str(octet)
           try:
               socket.setdefaulttimeout(1)
               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               s.connect((ip,port))
               output = s.recv(1024)
               print ("[+] The banner: %s for IP: %s at Port: %s" % (output,ip,port))
           except:
               print ("[-] Failed to Connect to %s:%s" % (ip, port))
           finally:
               s.close()

if __name__ == "__main__":
   main()