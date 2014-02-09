#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:17:03 2014

@author: zealot
"""

from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
import re,sys,subprocess,socket
from base_commond import *
import db
import subprocess
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

#开启多线程
env.parallel = 'true'

commond = sys.argv[1] 
argv = sys.argv[2]

if commond == "import":
    if os.path.isfile('./database/sabot.db'):
        db.import_info(sys.argv[2])
    else:
        db.init_database()
        db.import_info(sys.argv[2])
        env.passwords = db.make_connection_info()
        env.hosts = db.make_connection_info().keys()
elif commond == "check":
    if argv == "system_info":
        p = subprocess.Popen("fab -f base_commond.py system_monitor" ,shell = True,stdout = subprocess.PIPE)
        for i in  p.stdout.readlines():
            print i
    elif argv == "host_alive":
        p = subprocess.Popen("fab -f base_commond.py check_host_alive" ,shell=True,stdout = subprocess.PIPE)
        for i in p.stdout.readlines():
            print i
#由于在使用用户名@地址加端口的方式链接的时候可以不使用env.user这个环境变量，因此，一下只声明了几个基本的环境变量就可以了
#暂时注释，为了测试倒入功能
#env.passwords = db.make_connection_info()
#env.hosts = db.make_connection_info().keys()

#开启多线程
#env.parallel = 'true'



#commond = sys.argv[1] 
#argv = sys.argv[2]
#暂时先在文件检查这里只判断是否存在该文件，其他不判断
#if os.path.isfile('./database/sabot.db'):
#    pass 
#else: 
#    print "frist use robot.please init "


