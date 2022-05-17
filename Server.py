import socket
import time
from binascii import hexlify


ZERO = 0.025
ONE = 0.1

##Setup server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1337
s.bind(("", port))
s.listen(0)
print("Server is listening...")

c, addr = s.accept()

#Covert message
covert_message = "secret" + "EOF"
covert_bin = ''.join('{0:08b}'.format(ord(x), 'b') for x in covert_message)
print(covert_bin)
#Overt message
msg = "Some sort of overt message is being transmitted here. But there is a hidden message being covertly transmitted! Can you guess it?"

n=0
for i in msg:
    c.send(i.encode())
    if (covert_bin[n] == "0"):
        time.sleep(ZERO)
    else:
        time.sleep(ONE)
    n = (n + 1) % len(covert_bin)
c.send("EOF".encode())
c.close()
