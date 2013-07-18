#!/usr/bin/env python
# Filename:backup_ver2.py

import os
import time 

source=['/home/Emnawnrs', '/home/svnroot']
target_dir='/home/backup/'
today=target_dir+time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print 'successfully created directory', today
target=today+os.sep+now+'.zip'
zip_command="zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command)==0:
    print 'successful backup to', target
else:
    print 'backup failed'
