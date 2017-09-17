#!/usr/bin/env python

from __future__ import print_function

import sys
import subprocess
from datetime import datetime

__author__ = "Emanuele Disco"
__copyright__ = "Copyright 2017"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "emanuele.disco@gmail.com"
__status__ = "Production"

class Ttytter:
    """Ttytter class for sending twitter messages"""
    
    def init(self):
        pass
    
    def send(self, msg):
        """Send a twitter message"""
        now = datetime.utcnow()
        premsg = 'Raspi Alive: %s' % now.strftime('%Y-%m-%d %H:%M:%S')
        subprocess.Popen(['ttytter',
                          '-ssl',
                          '-autosplit',
                          '-hold',
                          '-status=%s  %s' % (premsg, msg)
                         ]
                        )
        
        
def _main(msg):
    Ttytter().send(msg or 'Testing my ttytter script')


if __name__ == '__main__':
    msg = None
    try:
        msg = sys.argv[1]
    except:
        pass
    
    _main(msg)