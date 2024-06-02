#!/usr/bin/python3
#services to auth to (smb, ldap, winrm, rdp, ftp, ssh, mssql)
import sys
import os


username = sys.argv[1]
password = sys.argv[2]
host = sys.argv[3]


print('Trying credentials against smb...')
print('======================================================================================================')
os.system(f'crackmapexec smb {host} -u {username} -p {password}')
print('======================================================================================================')

print('Trying credentials against ldap')
print('======================================================================================================')
os.system(f'crackmapexec ftp {host} -u {username} -p {password}')
print('======================================================================================================')

print('Trying credentials against ssh')
print('======================================================================================================')
os.system(f'crackmapexec ssh {host} -u {username} -p {password}')
print('======================================================================================================')

print('Trying credentials against winrm')
print('======================================================================================================')
os.system(f'crackmapexec winrm {host} -u {username} -p {password}')
print('======================================================================================================')

print('Trying credentials against rdp')
print('======================================================================================================')
os.system(f'crackmapexec rdp {host} -u {username} -p {password}')
print('======================================================================================================')

print('Trying credentials against mssql')
print('======================================================================================================')
os.system(f'crackmapexec mssql {host} -u {username} -p {password}')
print('======================================================================================================')
print('End.')
