#!/usr/bin/env python
import argparse, sys

def main():
    print sys.argv
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--event', action='store', dest='event', type=str, help='Event to trigger')
    parser.add_argument('-p', '--params', action='store', dest='params', type=str, help='Parameters to send with the event')
    args = parser.parse_args()

    print args
    
if __name__=='__main__':
    main()