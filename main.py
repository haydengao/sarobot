#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:17:03 2014

@author: zealot
"""

from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from optparse import OptionParser
import re,sys,subprocess,socket
import db
import subprocess
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

#开启多线程
env.parallel = 'true'

#检查数据库完整性和数据库文件状态
#db.check_database_status()
try:
    db.check_database_status()
except:
    print "init database!"
    db.init_database()


from base_commond import *

#构建命令参数列表

def main():
    parser = OptionParser()
    parser.add_option("--add", action = "store",  dest = "addserver", nargs = 4 )
    parser.add_option("--check", action = "store",  dest = "check_server_status")
    parser.add_option("--change_password", action = "store",  dest = "change_password", nargs = 2)
    parser.add_option("--display",action = "store", dest = "display_server_info")
    parser.add_option("--get", action = "store", dest = "file",nargs = 3)
    parser.add_option("--import", action = "store", dest = "importconfig", nargs = 1)
    parser.add_option("--push", action = "store",  dest = "file", nargs = 3)
    (options, args) = parser.parse_args()
    
    #if len(args) != 1:
    #    parser.error("incorrect number of arguments")
#    for i in options.addserver:
#        print i
        
#    print len(options.addserver)
    if options.addserver:
        db.add_server_info(options.addserver[0],options.addserver[1],options.addserver[2],options.addserver[3])
    if options.display_server_info:
        server_info = db.make_connection_info()
        for i in server_info:
            print i
    if options.change_password:
        server_info = db.make_server_info(options.change_password[0])
        env.user = server_info[0]
        env.password = server_info[1]
        env.host = options.change_password
        base_commond.change_password(options.change_password[1])
    if options.check_server_status:
        print options.check_server_status
        #这里需要增加一个功能，就是指定服务器的状态查询，暂时先放下，等所有流程跑通后在进行
        p = subprocess.Popen("fab -f base_commond.py system_monitor", shell = True, stdout = subprocess.PIPE)
        for i in p.stdout.readlines():
            print i
#    if options.change_password:
#        new_passwd = options.change_password[1]
#        print new_passwd
#        p = subprocess.Popen("fab -f base_commond.py change_password", shell = True, stdout = subprocess.PIPE)
        
    if options.importconfig:
        db.import_info(options.importconfig)#字典？字符？看明白了，这里如果使用的是多个参数，那么option的这个东西就变成了列表，否则就是字符串
        env.passwords = db.make_connection_info()
        env.hosts = db.make_connection_info().keys()
        
    

        




#commond = sys.argv[1] 
#argv = sys.argv[2]
#
#if commond == "import":
#    if os.path.isfile('./database/sabot.db'):
#        db.import_info(sys.argv[2])
#    else:
#        db.import_info(sys.argv[2])
#        env.passwords = db.make_connection_info()
#        env.hosts = db.make_connection_info().keys()
#elif commond == "check":
#    if argv == "system_info":
#        p = subprocess.Popen("fab -f base_commond.py system_monitor" ,shell = True,stdout = subprocess.PIPE)
#        for i in  p.stdout.readlines():
#            print i
#    elif argv == "host_alive":
#        p = subprocess.Popen("fab -f base_commond.py check_host_alive" ,shell=True,stdout = subprocess.PIPE)
#        for i in p.stdout.readlines():
#            print i
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
if __name__ == "__main__":
    main()

