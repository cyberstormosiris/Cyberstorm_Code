from datetime import datetime
import hashlib
import sys


for line in sys.stdin:
    ## USE STDIN TO READ IN EPOCH TIME

    #Format YYYY MM DD HH mm SS
    # %Y %m %d %H %M %S
    epoch_time = str(line).strip()
    #epoch_time = "1974 06 01 08 57 23" #"1999 12 31 23 59 59"
    epoch_datetime = datetime.strptime(epoch_time, '%Y %m %d %H %M %S')

    epoch_seconds = epoch_datetime.timestamp()
    ## USE CURRENT DATETIME AS SYSTEM TIME
    current_datetime = datetime.now()
    # Here's my code for setting current time manually
    #current_system_time =  "2017 04 26 15 14 30" #"2013 05 06 07 43 25"
    #current_datetime = datetime.strptime(current_system_time, '%Y %m %d %H %M %S')

    current_seconds = current_datetime.timestamp()
    ## GET TIME DIFFERENCE
    elapsed_time = current_seconds - epoch_seconds
    within_60 = elapsed_time % 60
    elapsed_time = elapsed_time - within_60

    elapsed_time_str = str(int(elapsed_time))

    output = hashlib.md5((hashlib.md5(elapsed_time_str.encode()).hexdigest()).encode()).hexdigest()
    print(output)
    print(output[((len(output))//2)] + output[((len(output))//2)+1])
    print(output[((len(output))//2)-1] + output[((len(output))//2)])
    nums = ''.join(filter(str.isdigit, output))
    chars = ''.join(filter(str.isalpha, output))
    final_output = chars[:2] + nums[-1] + nums[-2]
    print(final_output)
