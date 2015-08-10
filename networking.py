import socket

# This IP address is giving me a connection refused
# Find another IP address to use?

socket.setdefaulttimeout(10)
s = socket.socket()
try:
    s.connect(("192.168.95.148", 21))
except Exception, e:
    print "[] Error = " + str(e)
ans = s.recv(1024)
print ans

# print is supposed to return
# >> 220 FreeFloat FTP Server (version 1.0)

# 66.102.15.255 > google ip addres = time out
# 192.168.95.148 > book example
