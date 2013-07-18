#!/usr/bin/env python
# Filename:backup_ver1.py

import os
import time

source = ['/home/Emnawnrs', '/home/svnroot']
target_dir = '/home/backup/'
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr '%s' %s" % (target, ' ' .join(source))

if os.system(zip_command) == 0:
    print 'successful backup to', target
else:
    print 'backup failed'
