#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 14:42:07 2014

@author: zealot
"""

import sqlite3
import sys
from optparse import OptionParser


def parse():
    p = OptionParser()
    p.set_usage("command [options] file")
    p.add_option('import', dest = 'server_info_file', default = './server_info.txt')
    #p.add_option('-v', '--private', dest = 'vf')
#    p.add_option('add', dest = 'type', default = 'ssh-rsa')
    return p

conn = sqlite3.connect("./database/sabot.db")

sql_run = conn.cursor()
#创建用户名和密码的表
def init_database():
    sql_run.execute("create table account (id integer primary key UNIQUE, address varchar(20), username varchar(15),password varchar(100) , port integer default '22')")
    conn.commit()
#    sql_run.execute("")

#init_database()

#for i in [(0,'192.168.6.51','root','P@ssw0rd','22'),(1,"192.168.6.52","root","ayanami00","22")]:
#    sql_run.execute("insert into account values(?,?,?,?,?)",i)
    




def make_connection_info():
    server_account = {}
    sql_run.execute("select * from account")
    for k in sql_run.fetchall():
        server_account["%s@%s:%d" %(k[2],k[1],k[4])] = k[3]
        
    return server_account
#        print "%s@%s:%d" %(k[2],k[1],k[4])      

#def add_server():
#    server_info = []
    

def import_info():
    server_file = sys.argv[2]
    id = 0
    for server_info in open(server_file).readlines(100000):
        server_info_sql = []
        server_info_sql.append((id,str(server_info.split()[0]),server_info.split()[1],server_info.split()[2],server_info.split()[3]))
        print server_info_sql        
        for i in server_info_sql:
            sql_run.execute("insert into account values(?,?,?,?,?)",i)
            conn.commit()
#        server_host = str(server_info.split()[0])
#        server_user = server_info.split()[1]
#        server_passwd = server_info.split()[2]
#        server_port = server_info.split()[3]
        
#        print server_host ,server_user,server_passwd,server_port
#        sql_run.execute("insert into account values (%s,%s,%s,%s,%s,%s)" %(str(id),server_host,server_host,server_user,server_passwd,server_port))
#        conn.commit()
        id += 1

        

    
#if __name__ == "__main__":
#    main()
