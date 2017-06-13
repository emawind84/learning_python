#!/usr/bin/env python3

import json, csv, requests, logging, argparse, sys
import dateutil.parser

# ElasticSearch parameters
ES_HOST = '127.0.0.1'
ES_PORT = '9200'

# Lets make some logs!
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s')
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)

def post(index, typez, data):
    s = requests.Session()

    # let's prevent es from overwriting (creating new version) the same data if already exists
    # add the querystring: "op_type=create" to prevent from creating new version
    # https://www.elastic.co/guide/en/elasticsearch/guide/current/create-doc.html#create-doc
    r = s.post( "http://%s:%s/%s/%s?op_type=create" % 
              (ES_HOST, ES_PORT, index, typez), 
              data=json.dumps(data))
    
    _logger.debug(r.text)

def main():
    if not _args.data:
        _logger.error('Data missing, nothing to index!')
        return
    
    data = json.loads(_args.data)
    extra = json.loads(_args.extra or "{}")
    data.update(extra)
    post(_args.index, _args.typez, data)
      
if __name__=='__main__':
    _parser = argparse.ArgumentParser()
    _parser.add_argument('--data', action='store', dest='data', type=str, help='Data to send to elasticsearch')
    _parser.add_argument('--extra', action='store', dest='extra', type=str, help='Extra data to merge with the main data')
    _parser.add_argument('--index', action='store', dest='index', type=str, help='Index')
    _parser.add_argument('--type', action='store', dest='typez', type=str, help='Type')
    _parser.add_argument('-d', '--debug', action='store_true', dest='debug', help='More logging on console')
    _args = _parser.parse_args()
  
    if _args.debug:
        _logger.setLevel(logging.DEBUG)
       
    main()