#!/usr/bin/env python

from datetime import datetime

FILE_NAME = 'log.log'
WRITE_FREQ = 10

batch_data = []

def write_on_file():
    global batch_data
    with open(FILE_NAME, 'a') as f:
        print("Writing to file..")
        for line in batch_data:
            f.write(line + '\n')
        batch_data = []

def log(msg):
    dt = datetime.utcnow()
    datestr = dt.strftime('%Y-%m-%d %H:%M:%S')
    batch_data.append('[%s] %s' % (datestr, msg))
    if len(batch_data) >= WRITE_FREQ:
        write_on_file()
    
def main():
    log('This is a test message! Ciao!')
    
if __name__=='__main__':
    main()