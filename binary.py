#Osiris Team binary decoding program
#Written originally by Dustin Smith

#input grab
binaryString = input("Input binary string: ")
#checks if the message is encoded in ASCII 7 or binary 8 via modulus
if(len(binaryString)%8==0):
    ASCIISize = 8
elif(len(binaryString)%7==0):
    ASCIISize = 7
#indexes the string based on previously found length, converts to int, then uses
#python's built in chr() operator to convert to unicode/ascii format
charList = []
for i in range(0,len(binaryString),ASCIISize):
    charList.append(chr(int(binaryString[i:i+ASCIISize],2)))
#finally joins these characters together and outputs result
print("Output: "+"".join(charList))


