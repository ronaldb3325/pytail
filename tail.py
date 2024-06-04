import os
import time
import sys

def follow(thefile):
    while True:
        line = thefile.readline()
        if not line or not line.endswith('\n'):
            time.sleep(0.1)
            continue
        yield line

def tail(filen):
    logfile = open(filen,"r")
    loglines = follow(logfile)
    for line in loglines:
        print(line, end='')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please define the filename as parameter")
        print("bitte Dateinamen als Parameter angeben.")
    else:
        ifile=sys.argv[1]
        tail(ifile)