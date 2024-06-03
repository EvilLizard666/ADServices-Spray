#!/usr/bin/python3
#services to auth to (smb, ldap, winrm, rdp, ftp, ssh, mssql)
import sys
import os


host = sys.argv[1]
username  = sys.argv[2]
password = sys.argv[3]


print('Trying credentials against smb...')
print('======================================================================================================')
os.system(f'netexec smb {host} -u {username} -p {password}')
print('======================================================================================================')

print('Trying credentials against ldap')
print('======================================================================================================')
os.system(f'netexec ftp {host} -u {username} -p {password}')
print('======================================================================================================')

print('Trying credentials against ssh')
print('======================================================================================================')
os.system(f'netexec ssh {host} -u {username} -p {password}')
print('======================================================================================================')

print('Trying credentials against winrm')
print('======================================================================================================')
os.system(f'netexec winrm {host} -u {username} -p {password}')
print('======================================================================================================')

print('Trying credentials against rdp')
print('======================================================================================================')
os.system(f'netexec rdp {host} -u {username} -p {password}')
print('======================================================================================================')

print('Trying credentials against mssql')
print('======================================================================================================')
os.system(f'netexec mssql {host} -u {username} -p {password}')
print('======================================================================================================')
print('End.')
