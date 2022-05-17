import sys
import re
sentinel = bytearray(b'\x00\xff\x00\x00\xff\x00')

## functions 
#function for byte retrieval
def byte_Retrieve(wrap, sentinel, offset, interval):
    #read wrapper bytes
    wrap_file = open(wrap, "rb")
    wrap_bytes = bytearray(wrap_file.read())
    wrap_file.close()

    
    #empty byte array
    hidden_bytes = bytearray()

    
    while(offset < len(wrap_bytes)):
        b = wrap_bytes[offset]
        #checks if b matches a sentinel, if so break from the loop otherwise ,
        #add b to hidden_bytes

        #turn into an actual byte
        b = b.to_bytes(1, 'big')
        #add to byte array 
        hidden_bytes += b
        #if sentinel is detected, remove it's data from the message andstop
        if hidden_bytes[-len(sentinel):] == sentinel:
            hidden_bytes=hidden_bytes[:-len(sentinel)]
            break
        #offset += interval
        offset += interval
        
    #output
    sys.stdout.buffer.write(hidden_bytes)

def byte_Storage(wrap, hidden, sentinel, offset, interval):
    # read files as byte arrays
    wrap_file = open(wrap, "rb")
    wrap_bytes = bytearray(wrap_file.read())
    wrap_file.close()
    hidden_file = open(hidden, "rb")
    hidden_bytes = bytearray(hiddenFile.read())
    hidden_file.close()
    
    i = 0
    j = 0
    # store hidden bytes in wrap file
    while(i < len(hidden_bytes)):
        wrap_bytes[offset] = hidden_bytes[i]
        offset += interval
        i += 1
        
    # add sentinel bytes
    while(j < len(sentinel)):
        wrap_bytes[offset] = sentinel[j]
        offset += interval
        j += 1
    # output
    sys.stdout.buffer.write(wrap_bytes)


#function for bit storage
def bit_Storage(wrap, hidden, sentinel, offset, interval):
    # read files as byte arrays
    wrap_file = open(wrap, "rb")
    wrap_bytes = bytearray(wrapFile.read())
    wrap_file.close()
    hidden_file = open(hidden, "rb")
    hidden_bytes = bytearray(hidden_file.read())
    hidden_file.close()
    i = 0
    j = 0
    #store in wrap files
    while (i < len(hidden_bytes)):
        for n in range(8):
            wrap_bytes[offset] &= 0b11111110
            wrap_bytes[offset] |= ((hidden_bytes[i] & 0b10000000) >> 7)
            hidden_bytes[i] = (hidden_bytes[i] << 1) & (2 ** 8 - 1)
            offset += interval
        i += 1
    # add sentinel bytes
    while (j < len(sentinel)):
        for n in range(8):
            wrap_bytes[offset] &= 0b11111110
            wrap_bytes[offset] |= ((sentinel[j] & 0b10000000) >> 7)
            sentinel[j] = (sentinel[j] << 1) & (2 ** 8 - 1)
            offset += interval
        j += 1
    #output
    sys.stdout.buffer.write(wrap_bytes)

def bit_Retrieve(wrap, sentinel, offset, interval):
    #read file as byte array
    wrap_file = open(wrap, "rb")
    wrap_bytes = bytearray(wrap_file.read())
    wrap_file.close()
    #make empty bytearray to put hidden bytes in
    hidden_bytes = bytearray()
    while offset < len(wrap_bytes):
        #hidden byte to be constructed
        b = 0
        for i in range(8):
            #max of 1889858
            #print(i,offset)
            #get least significan bit of current byte
            b |= (wrap_bytes[offset] & 0o0000001)
            if i < 7:
                # bitshift byte by one and prevent overflow
                b = (b << 1) & (2 ** 8 - 1)
                #move to the  next byte
                offset += interval
            if(offset >= len(wrap_bytes)):
                break
                
        #turn into an actual byte
        b = b.to_bytes(1, 'big')
        
        #add to byte array
        hidden_bytes += b
        #if sentinel is found, break
        if hidden_bytes[len(hidden_bytes) - len(sentinel):] == sentinel:
            break
        offset += interval
    #output
    sys.stdout.buffer.write(hidden_bytes)
    



    

##Main Program

## get users' input 
    
if len(sys.argv)>4: #checks if minimum input of 4 is provided
    
    wrap =""
    #checks if the first input is s or r (store or retrieve)
    if(sys.argv[1] == "-s" or sys.argv[1] == "-r"):
        mode = sys.argv[1][1:]
        
    else: # else 
        print("Please use -s for Store and -r for Retrieve mode")
        exit(0)
        

    #checks if the second input is a bit or byte, and stores the value
        #into a variable called type_mode
   
    if(sys.argv[2] == "-b" or sys.argv[2] == "-B"):
        type_mode = sys.argv[2][1:]
        
    else: # else 
        print("Please use -b for bit and -B for byte mode")
        exit(0)
        

    #checks if an offset is provided by the user, and stores the value
        #provided into a variable called offset
        
    if(sys.argv[3][0:2] == "-o"):
        offset = sys.argv[3][2:]

        #if there is an offset but no value set offset to 0 default value
        if(offset ==""):
            offset = "0"
            
    else: # else
        print("Please use -o<val> set offset to <val> (defualt is 0)")
        exit(0)


    #checks if an interval or a wrapper is provided by the user, and stores the value
        #provided into a variable called interval
        
  
    if(sys.argv[4][0:2] == "-i"):  
        interval = sys.argv[4][2:]

        #if there is no value provided, set the interval to default (1)
        if(interval == ""):
           interval = "1"

           
    elif(sys.argv[4][0:2] == "-w"): 
           wrap = sys.argv[4][2:]
           interval ="1"

           
    else: 
        print("please use -i<val> set interval to <val> (defualt is 1)")
        print("or -w<val> set wrapper file to <val>")
        exit(0)


    
    if(len(sys.argv)>5): #checks if there are more input
        if(wrap == sys.argv[4][2:]): # if wrap has been made
            if(sys.argv[5][0:2] == "-h"): # if there 
                hidden = sys.argv[5][2:]
                
            else: # default
                hidden = ""
                
        else: 
            if(sys.argv[5][0:2] == "-w"): # if there 
                wrap = sys.argv[5][2:]
                
            else:
                print("Please use -w<val> set wrapper file to <val>")
                exit(0)
                
            if(len(sys.argv)>6): # if there are more inputs 
                if(sys.argv[6][0:2] == "-h"): # if there 
                    hidden = sys.argv[6][2:]
                else: # default
                    hidden = ""
            else: # else if there are no more inputs 
                hidden = ""   
    else:
         hidden =""   

    #converts offset and interval into integers 
    offset = int(offset)
    interval = int(interval)
    
else: #if user input is less than 4 
    print("INVALID Input:")
    print("Python3 "+ sys.argv[0] + " -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]")
    exit(0)


#all combinations of modes; checks for -s and -b, -r and -b,
#-s, -B, -r, B
if (sys.argv[1] == "-s" and sys.argv[2] == "-b"):
    #call bitstorage function
    bit_Storage(wrap, hidden, sentinel, offset, interval)

    
if (sys.argv[1] == "-r" and sys.argv[2] == "-b"):
    bit_Retrieve(wrap, sentinel, offset, interval)
    
if (sys.argv[1] == "-s" and sys.argv[2] == "-B"):
    #call bytestorage function
    byte_Storage(wrap, hidden, sentinel, offset, interval)
    
if (sys.argv[1] == "-r" and sys.argv[2] == "-B"):
    #call byte retrieval function
    byte_Retrieve(wrap, sentinel, offset, interval)

