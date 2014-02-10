#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 14:42:07 2014

@author: zealot
"""

import sqlite3
import sys
from optparse import OptionParser
import os


#def parse():
#    p = OptionParser()
#    p.set_usage("command [options] file")
#    p.add_option('import', dest = 'server_info_file', default = './server_info.txt')
#    #p.add_option('-v', '--private', dest = 'vf')
##    p.add_option('add', dest = 'type', default = 'ssh-rsa')
#    return p


#创建用户名和密码的表
def init_database():
    conn = sqlite3.connect("./database/sabot.db")
    sql_run = conn.cursor()
    #sql_run.execute("create table account (id integer primary key UNIQUE, address varchar(20), username varchar(15),password varchar(100) , port integer default '22')")
    sql_run.execute("create table account (address varchar(20), username varchar(15),password varchar(100) , port integer default '22')")
    conn.commit()
    conn.close()



def make_connection_info():
    conn = sqlite3.connect("./database/sabot.db")
    sql_run = conn.cursor()
    server_account = {}
    sql_run.execute("select * from account")
    for k in sql_run.fetchall():
        server_account["%s@%s:%d" %(k[1],k[0],k[3])] = k[2]
    
    return server_account

    

def import_info(server_file):
#这里参数2提供的目录路径硬要写完整，绝对路径没有问题，相对路径一定要加上./否则不会插入内容
#    server_file = sys.argv[2]
#    server_file = "./conf/test.txt"
    conn = sqlite3.connect("./database/sabot.db")
    sql_run = conn.cursor()
    #id = 0
    for server_info in open(server_file).readlines(100000):
        server_info_sql = []
        server_info_sql.append((str(server_info.split()[0]),server_info.split()[1],server_info.split()[2],server_info.split()[3]))
        print server_info_sql        
        for i in server_info_sql:
            #sql_run.execute("insert into account values(?,?,?,?,?)",i)
            sql_run.execute("insert into account values(?,?,?,?)",i)
            conn.commit()

        #id += 1

    conn.close()

#def add_server_info()
