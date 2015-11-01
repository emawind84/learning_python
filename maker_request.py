#!/usr/bin/env python
import requests, argparse, json

maker_key = 'nmr2BnBoPJPDkNvfz3bk0'

parser = argparse.ArgumentParser()
parser.add_argument('-e', action='store', dest='event', type=str, help='Event to trigger')
parser.add_argument('-p', action='store', dest='params', type=str, help='Parameters to send with the event')
args = parser.parse_args()

def send(event, params=None):
    # https://maker.ifttt.com/trigger/{event}/with/key/nmr2BnBoPJPDkNvfz3bk0
    r = requests.get("https://maker.ifttt.com/trigger/%s/with/key/%s" % (event, maker_key), data=params)
    r.text
    
def main():
    if not args.event:
        print('Event not defined')
        return
    if args.params:
        try:
            p = json.loads(args.params)
        except:
            print('Parameters not well format. JSON format required.')
            return
    send(args.event, p)
    
if __name__=='__main__':
    main()