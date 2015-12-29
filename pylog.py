#!/usr/bin/env python
from __future__ import print_function, division
from datetime import datetime
import atexit, os.path

FILE_NAME = 'log.log'
WRITE_FREQ = 10

batch_data = []

def _get_filename():
    return FILE_NAME

def set_header(header):
    print('Setting header...')
    if os.path.isfile(_get_filename()):
        raise Exception('Logging file already exists!')
        
    with open(_get_filename(), 'w') as f:
        f.write(','.join(str(value) for value in header) + '\n')

def write_on_file():
    global batch_data
    with open(_get_filename(), 'a') as f:
        print("Writing log to file...")
        for line in batch_data:
            f.write(line + '\n')
        batch_data = []
        
def log_data(data):
    out = ','.join(str(value) for value in data)
    batch_data.append(out)
    if len(batch_data) >= WRITE_FREQ:
        write_on_file()

def log(msg):
    dt = datetime.utcnow()
    datestr = dt.strftime('%Y-%m-%d %H:%M:%S')
    batch_data.append('[%s] %s' % (datestr, msg))
    if len(batch_data) >= WRITE_FREQ:
        write_on_file()
    
def main():
    log('This is a test message! Ciao!')
    
atexit.register(write_on_file)
    
if __name__=='__main__':
    main()