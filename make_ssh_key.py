#! /usr/bin/env python


import pexpect

make_key = pexpect.spawn('ssh-keygen')
make_key.expect('Generating public*:')
make_key.sendline("\r\n")
make_key.expect('Enter passphrase (empty for no passphrase):')
make_key.sendline("\r\n")
make_key.expect('Enter same passphrase again:')
make_key.sendline("\r\n")

