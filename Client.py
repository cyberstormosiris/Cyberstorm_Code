import socket
import sys
from time import time
from binascii import unhexlify

DEBUG = False

#Hardcoded zero and one values
ONE = 0.2
ZERO = 0.1

#IP and Port numbers
ip = "10.0.0.125"
port = 12321

#Connecting to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
sys.stdout.write("[connect to the chat server]\n")
#Get first bit of data
data = s.recv(4096).decode()

sys.stdout.write("...\n")
sys.stdout.flush()
covert_bin = ""
while ((data.rstrip("\n")) != "EOF"): #Recieve data until EOF comes
    sys.stdout.write(data)
    sys.stdout.flush()

    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()

    delta = round(t1 - t0, 3) # why 3?
    if DEBUG:
        sys.stdout.write(" "+str(delta)+"\n")
        sys.stdout.flush()
    if (delta >= ONE):
        covert_bin += "1"
    else:
        covert_bin += "0"


if DEBUG:
    print(covert_bin)

sys.stdout.write("...\n")
sys.stdout.flush()
sys.stdout.write("[disconnect from the chat server]\n")
sys.stdout.flush()
s.close()

#Translate covert message
covert = ""
i = 0
while (i < len(covert_bin)):
    # process one byte at a time
    b = covert_bin[i:i + 8]
    # convert it to ASCII
    n = int("0b{}".format(b), 2)
    try:
        #covert += unhexlify("{0:x}".format(n))
        covert += chr(int(b, 2))
    except TypeError:
        covert += "?"
    # stop at the string "EOF"
    if covert[-3:] == "EOF":
        covert = covert[:-3]
        break
    i += 8
sys.stdout.write("Covert message: " + covert+"\n")