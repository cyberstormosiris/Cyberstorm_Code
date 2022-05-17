from math import ceil

DEBUG = True


password = input()
timings = input()

password = password.split(',')
timings = timings.split(',')

if DEBUG:
    print(f"password = {password}")
    print(f"timings = {timings}")

psswrd = "".join(password[:ceil(len(timings)/2)])
kpt = [float(x) for x in timings[:ceil(len(timings)/2)]]
kht = [float(x) for x in timings[ceil(len(timings)/2):]]

if DEBUG:
    print(psswrd)
    print(kpt)
    print(kht)
