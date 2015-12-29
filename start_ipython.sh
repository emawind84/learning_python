#!/bin/bash

SCRIPT_BASE_PATH=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
SCRIPT_NAME="${0##*/}"

export PATH=$SCRIPT_BASE_PATH/ipython/bin:$PATH

set -e

echo "Script name: [$SCRIPT_NAME]"
echo "Base path: [$SCRIPT_BASE_PATH]"
echo "Starting iPython notebook..."

cd $SCRIPT_BASE_PATH

ipython notebook >/dev/null 2>&1 &
#ipython notebook
