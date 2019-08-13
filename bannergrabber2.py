#banner Grabber 2 - Write To File

#Write a tool that takes in two command line arguments, ip & port, and
#attempts to connect and perform a banner grab.  If the connection is successful,
#and a banner is returned, store the information in a text file.  Include
#error handling for the case that the attempted socket connection fails
#or if there is an error writing to the text file.

#Write your code here.....

import socket
import sys

def bannerGrab(ip, port):
   try:
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.connect((ip,port))
       output = s.recv(1024)
       outputBanner(output,ip,port)
   except:
       print("[-] Failed to connect to %s:%s” % (ip,port)")

def outputBanner(output,ip,port):
   try:
       f=open('Banner.txt', 'r')
       infoForFile=(str(ip) +":" + str(port) + " is running the following service: " + str(output))
       f.write(f(infoForFile))
       f.exit()
       print("[+] Success.  Banner.txt was created. \nGoodbye.")
   except:
       sys.exit("Error writing file")


def main():
   ip = sys.argv[1]
   port = sys.argv[2]
   bannerGrab(ip,port)

if __name__ == "__main__":
   main()

