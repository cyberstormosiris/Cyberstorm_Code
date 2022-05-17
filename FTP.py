from ftplib import FTP

DEBUG = False


IP = "138.47.128.12"
PORT = 21
USER = ""
PASSWORD = "EncryptionGods"
FOLDER = "/files"
USE_PASSIVE = True
METHOD = 7


ftp = FTP()
ftp.connect(IP,PORT)
ftp.login(USER,PASSWORD)
ftp.set_pasv(USE_PASSIVE)

ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

ftp.quit()

#create a list of strings that originally will hold the translated binary text,
#and then be dynamically converted to an ascii character
filesBinary = []
for f in files:
    #we only need the first 10 characters of the FTP readout
    f=f[:10]
    #Debug print the current file
    if(DEBUG):
        print(f)
    #if we are doing 7 bit encoding
    if METHOD == 7:
        #ignore anything that doesn't start with ---
        if f[:3] == "---":
            #we need to create a new binary string entry
            filesBinary.append("")
            binary = ''.join("1" if c in ["d", "r", "w", "x"] else "0" for c in str(f[3:]))
            filesBinary[-1] = (chr(int(binary, 2)))
    #10 bit method
    else:
        #if this is the first file perm to be read overall, we create our first
        #binary string
        if len(filesBinary)==0:
            filesBinary.append("")
        for i in range(0,10):
            #same translation method as 7 bit, but using the entire 10 bit string
            if f[i] == "-":
                filesBinary[-1]+="0"
            else:
                filesBinary[-1]+="1"
            #once our current binary string reaches 7 bits long, regardless of
            #our position in the perm string, we translate those 7 bits into an
            #ASCII char and create a new contrainer
            
            if len(filesBinary[-1])==7:
                filesBinary[-1]=chr(int(filesBinary[-1],2))
                filesBinary.append("")
            
#finally, print out all our translated ASCII chars  
print("".join(filesBinary))