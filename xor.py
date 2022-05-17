#Team Osiris XOR Encryption Program
#Takes byte data from stdin, reads bytes from a key file,
#XOR's them together, then outputs to stdout
import sys
DEBUG = False
#read input byte data. stdin.buffer.read() returns raw bytes, which is helpful here
varBytes = sys.stdin.buffer.read()
if DEBUG:
    print(varBytes)
    print()
#open enables you to read a file as a binary type, meaning no conversion necessary
keyFile = open("22_00","rb")
keyBytes = keyFile.read()
keyFile.close()
if DEBUG:
    print(keyBytes)
    print()
#the main code, pretty simple. Make a list, append each XOR'd byte value together'
encrypted = []
for i in range(len(varBytes)):
    encrypted.append(varBytes[i]^keyBytes[i])
    #if DEBUG:
        #print(i,varBytes[i],keyBytes[i],encryptedBytes[i])
#the bytes() function changes the list into a long bytes type object,
#then we write to stdout via buffer.write, which also drops the b'' that print would have.'
sys.stdout.buffer.write(bytes(encrypted))