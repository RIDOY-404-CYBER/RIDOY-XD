
#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
 print(f'\033[1;34m [•] Join Facebook Public Group')
os.system('xdg-open https://facebook.com/groups/3017062245271082/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf RMX3.so')
except:
    pass
os.system('rm -rf RMX3.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
	print('\033[1;34m\n Congratulations! Your Device Support This Tools\033[1;37m')
    if not os.path.isfile('RMX3.so'):
        os.system('curl -L https://github.com/RIDOY-404-CYBER/RIDOY-XD/blob/main/RMX3.cpython-311.so?raw=true -o RMX3.so') 
        import RMX3
    else:
        import RMX3
        
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
