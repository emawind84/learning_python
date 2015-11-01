#!/bin/bash

curl -H "Content-Type: application/json" \
     -X POST \
     -d '{"value1": "10000"}' \
     https://maker.ifttt.com/trigger/noise_detected/with/key/nmr2BnBoPJPDkNvfz3bk0

echo -e '\nScript Terminated'
