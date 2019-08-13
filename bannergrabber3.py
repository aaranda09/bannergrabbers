"""
Banner_Grabber_Mult.py

Write a tool that attempts to connect to user defined IP addresses and ports on remote
targets, requests banners, and store the results in a text file. This script must take
in user input as long as the user continues to indicate, through input (‘y’ or ‘n’),
that they have more targets to test.  Once the user types ‘n’, the script should provide
a closing message and exit.  While the user indicates that they would like to continue
submitting targets, take user input and use it to banner grab the desired IP address
and port.  A function should be included that stores the results of successful banner
grabs in a .txt file.  It is important that each successive test does not send the
results to a function that overwrites rather than append to a .txt file.  Make sure
to include error handling.

"""

import socket
import sys

def bannerGrab(ip, port):
   try:
       socket.setdefaulttimeout(1)
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.connect((ip,port))
       output = s.recv(1024)
       outputBanner(output,ip,port)
   except:
       print("[-] Failed to connect to %s:%s" % (ip,port))

def outputBanner(output,ip,port):
   try:
       f=open("Banners.txt", "r")
       infoForFile=(str(ip) +":" + str(port) + " is running the following service: " + str(output))
       f.write(f(infoForFile))
       f.exit()
       print("[+] Success.  Banner added to BannerTargets.txt")
   except:
       sys.exit("Error writing file")

def main():
   answer = input("Would you like to input and ip address and port?(y or n): ")
   while answer == "y":
       ip = input("\nWhat IP would you like to target? ")
       port = input("What is the port you would like to target? ")
       bannerGrab(ip,port)
       answer = input("Continue? y or n: ")

   print("Goodbye.")

if __name__ == "__main__":
   main()

#message Input


#Message #learning