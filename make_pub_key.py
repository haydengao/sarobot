#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 18:31:32 2014

@author: zealot
"""


import struct
import base64
import sys
import os
from optparse import OptionParser
from Crypto.PublicKey import RSA
def get_bin(n):
    s = ''
    n = long(n)
    while (n != 0) and (n != -1):
        s = struct.pack('>I', n & 0xffffffffL) + s
        n = n >> 32
          
    for i in enumerate(s):
        if (n == 0) and (i[1] != '\000'):
            break
        if (n == -1) and (i[1] != '\xff'):
            break
          
    s = s[i[0]:]
    if (n == 0) and (ord(s[0]) >= 0x80):
        s = '\x00' + s
    if (n == -1) and (ord(s[0]) <0x80):
        s = '\xff' + s
          
    s = struct.pack(">I", len(s)) + s
    return s
def parse():
    p = OptionParser()
    p.set_usage("command [options] privatekey")
    p.add_option('-p', '--publickey', dest = 'publickey', default = './p.pub')
    #p.add_option('-v', '--private', dest = 'vf')
    p.add_option('-t', '--type', dest = 'type', default = 'ssh-rsa')
    return p
def main():
    p = parse()
    options, args = p.parse_args()
         
    try:
        vf = args[0]
    except IndexError:
        print "Please use '-h/--help' for help!"
        sys.exit(1)
    try:
     f = open(vf)
    except IOError, e:
        print e
        sys.exit(1)
          
    uf = options.publickey
    if os.path.exists(uf):
        print "%s is exists!" % uf
        sys.exit(1)
    try:
        k = RSA.importKey(f.read())
    except ValueError, e:
        print e
        sys.exit(1)
    s = ''
    t = options.type
    l = len(t)
    s = struct.pack('>I%ss' % l, l, t)
    e = get_bin(k.e)
    n = get_bin(k.n)
    b = base64.b64encode(''.join((s, e, n)))
          
    try:
        of = open(uf, 'w')
        of.write("%s %s\n" % (t, b))
        of.close()
    except IOError, e:
        print e
        sys.exit(1)
if __name__ == "__main__":
    main()
