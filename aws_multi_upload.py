#!/usr/bin/env python3

import requests, argparse, json, logging, sys, os, sha256_tree_hash, codecs
import subprocess, es_data_import
from datetime import datetime

BACKUP_TEMP_FOLDER='/media/usb2/backup'
PART_SIZE=67108864
AWS_VAULT='raspi'
ES_METADATA_INDEX='aws-vault'
ES_METADATA_TYPE='archive'
AWS_PATH='/home/pi/bin/aws'

ARCHIVE_PREFIX='{}/archive.gz.part_'.format(BACKUP_TEMP_FOLDER)
_args = {}
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s')
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)

def _start_request():
    out = subprocess.check_output([AWS_PATH, 
                        "glacier", 
                        "initiate-multipart-upload", 
                        "--vault-name={}".format(AWS_VAULT), 
                        "--account-id=-", 
                        "--archive-description=test", 
                        "--part-size=%s" % PART_SIZE ])
    return json.loads(out.decode('UTF-8'))['uploadId']

def _complete_request(upload_id, checksum):
    stats = os.stat(_args.file)
    archive_size = stats.st_size
    out = subprocess.check_output([AWS_PATH, 
                        "glacier", 
                        "complete-multipart-upload", 
                        "--vault-name={}".format(AWS_VAULT), 
                        "--account-id=-",
                        "--checksum=%s" % checksum,
                        "--upload-id=%s" % upload_id,
                        "--archive-size=%s" % archive_size ])
    return out.decode('UTF-8')

def _import_to_es(data, description="", filename="archive"):
    now = datetime.now()
    data = json.loads(data)

    data.update({ 
        "description": description, 
        "filename": filename, 
        "timestamp": now.strftime('%Y-%m-%dT%H:%M:%S.%f%z') })
    _logger.debug(data)

    response = es_data_import.post( ES_METADATA_INDEX, ES_METADATA_TYPE, data )
    return response.text

def _multi_upload(filename, upload_id):
    stats = os.stat(_args.file)
    archive_size = stats.st_size
    parts = archive_size // PART_SIZE
    if archive_size % PART_SIZE > 0:
        parts += 1
        
    sha256_parts = []
    dd = subprocess.Popen(['dd', 
          'if=%s' % filename, 
          'bs=2M']
         , stdout=subprocess.PIPE )
    
    out = subprocess.check_output(['split', 
          '--suffix-length=1', 
          '--numeric-suffixes=0', 
          '--bytes=%s' % PART_SIZE, 
          '-', 
          ARCHIVE_PREFIX]
         , stdin = dd.stdout )
    
    start=0
    end=0
    for i in range(parts):
        part_filename = ARCHIVE_PREFIX + str(i)
        start = start * PART_SIZE
        stats = os.stat(part_filename)
        end = start + stats.st_size - 1
        
        chunks = sha256_tree_hash.get_chunks_sha256_hashes(part_filename)
        checksum = sha256_tree_hash.compute_sha256_tree_hash(chunks)
        sha256_parts.append(codecs.getdecoder('hex')(checksum)[0])
        
        subprocess.call([AWS_PATH,
              'glacier', 
              'upload-multipart-part',
              '--vault-name={}'.format(AWS_VAULT),
              '--account-id=-',
              '--body', part_filename,
              '--upload-id', str(upload_id),
              '--checksum', checksum,
              '--range', 'bytes {}-{}/*'.format(start, end)])
        start += 1

    complete_checksum = sha256_tree_hash.compute_sha256_tree_hash( sha256_parts )
    return complete_checksum

def upload(filename, description):
    upload_id = _start_request()
    _logger.debug('Requested Upload Id: {}'.format(upload_id))
    checksum = _multi_upload(filename, upload_id)
    _logger.debug('Full sha256 tree hash: {}'.format(checksum))
    aws_response = _complete_request(upload_id, checksum)
    _logger.debug('Upload Complete request response: {}'.format(aws_response))
    es_response = _import_to_es(aws_response, filename=filename, description=description)
    _logger.debug('ES import response : {}'.format(es_response))

    return aws_response
    
def _main():
    upload(_args.file, _args.descr)

if __name__=='__main__':   
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-f', action='store', dest='file', type=str, help='File to upload')
    _parser.add_argument('-m', action='store', dest='descr', type=str, help='Description')
    _parser.add_argument('-d', '--debug', action='store_true', dest='debug', help='More logging on console')
    _args = _parser.parse_args()
    
    if _args.debug:
        _logger.setLevel(logging.DEBUG)
    
    _main()