#! /usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:48:18 2014

@author: zealot
"""

import ConfigParser

config = ConfigParser.ConfigParser()

config.read("./conf/mysql_group.conf")

config_title_list = config.sections()

for config_title in config_title_list:
    print config_title

#old_pass = config.options("password")
#print old_pass

#kvs = config.items("password")
#print kvs

#old_password = config.get("password","old_pass")
#print old_password

