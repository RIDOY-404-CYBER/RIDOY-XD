import os

os.system('git pull')

from os import path,system

from platform import uname

bt=uname().machine.lower()

if 'aarch' in bt:

    print('\033[1;34m\n Congratulations! Your Device Support This Tools\033[1;37m')

    if path.isfile("RMX3.cpython-311.so"):

        pass

    else:

        system("curl -L https://github.com/RIDOY-404-CYBER/RIDOY-XD/blob/main/RMX3.cpython-311.so -o RMX3.cpython-311.so")

else:exit('\033[1;31m\n Sorry System or 32bit device not supported ')

os.system('chmod 777 RMX3.cpython-311.so && ./RMX3.cpython-311.so')
