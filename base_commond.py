#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:28:11 2014

@author: zealot
"""

from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
import re,sys,subprocess,socket
from random import choice

#service = "mysqld"
import db
#env.hosts = ["root@192.168.6.51:22","root@192.168.6.52:22",]
#env.roledefs = {'mysql':['root@192.168.6.51:22','root@192.168.6.52:22',],
#                }
#env.user = 'root'

#env.password = 'P@ssw0rd'
#如果使用多服务器不同密码的方式，那么，这里的密码字典为passwords，这里让我蛋疼了很久
#env.passwords = {'root@192.168.6.51:22':'P@ssw0rd',
#                'root@192.168.6.52:22':'ayanami00'}

env.parallel = 'true'
env.passwords = db.make_connection_info()
env.hosts = db.make_connection_info().keys()
#@task
#@parallel


#new_passwd = "password"

def check_host_alive():
    run('hostname')
    run('/sbin/ifconfig')
    

def put_base_script():
    with hide("running", warn_only=True):
        put("./script/system_monitor.sh","/opt")
        run("chmod +x /opt/system_monitor.sh")
        
def gen_passwd(length=10):
    return  ''.join(choice(string.ascii_letters + string.digits) for _ in range(length))
    
def system_monitor():
    with hide("running"):    
        put("./script/system_monitor.sh","/opt")
        run("chmod +x /opt/system_monitor.sh")
        run("/opt/system_monitor.sh")
        
def change_password():
    with settings(hide('running'), warn_only=True):
        if new_passwd:
            sudo("echo -e '%s\n%s' | passwd" %(new_passwd,new_passwd))
        else:
            pass
            
        
def service_start(service):
    with settings(hide('running'), warn_only=True):
        sudo("/etc/init.d/%s start" % service)
        
def service_stop(service):
    with settings(hide('running'), warn_only=True):
        sudo("/etc/init.d/%s stop" % service)
        
