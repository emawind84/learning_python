#!/usr/bin/env python
import requests, argparse, json, logging, sys

_maker_key = 'nmr2BnBoPJPDkNvfz3bk0'
_args = {}

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s')
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)

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
    print sys.argv
    
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-e', action='store', dest='event', type=str, help='Event to trigger')
    _parser.add_argument('-p', action='store', dest='params', type=str, help='Parameters to send with the event')
    _parser.add_argument('-d', '--debug', action='store_true', dest='debug', help='More logging on console')
    _args = _parser.parse_args()
    
    if _args.debug:
        _logger.setLevel(logging.DEBUG)

    _logger.debug("event: %s" % _args.event)
    _logger.debug("params: %s" % _args.params)
    
    main()