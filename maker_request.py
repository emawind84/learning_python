#!/usr/bin/env python
import requests, argparse, json

_maker_key = 'nmr2BnBoPJPDkNvfz3bk0'
_args = {}

def send(event, params=None):
    # https://maker.ifttt.com/trigger/{event}/with/key/nmr2BnBoPJPDkNvfz3bk0
    r = requests.get("https://maker.ifttt.com/trigger/%s/with/key/%s" % (event, _maker_key), data=params)
    r.text
    
def main():
    if not _args.event:
        print('Event not defined')
        return
    if _args.params:
        try:
            p = json.loads(_args.params)
        except:
            print('Parameters not well format. JSON format required.')
            return
    send(_args.event, p)
    
if __name__=='__main__':
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-e', action='store', dest='event', type=str, help='Event to trigger')
    _parser.add_argument('-p', action='store', dest='params', type=str, help='Parameters to send with the event')
    _args = _parser.parse_args()

    main()