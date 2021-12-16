import os
import time
from pwd import getpwuid

pswdfile = open('/etc/passwd', 'r')
newContent = ''
#1------------------------------
for line in pswdfile:
    newContent += line

newContent += '-----------------------------------\n'
#2--------------------------------
for root, dirs, files in os.walk("/var"):
    for file in files:
        if ((file == "messages") or (file == "secure") or (file == "auth.log")):
            stats = os.stat(os.path.join(root, file))
            newContent += "File: " + os.path.join(root, file) + "\n"
            newContent += "File Size: " + str("{:.2f}".format(stats.st_size/1024.0)) + "KB\n"
            newContent += "File Owner: " + getpwuid(stats.st_uid).pw_name + "\n"
            newContent += "Last Modified: " + time.ctime(stats.st_mtime) + "\n"
            newContent += "Permisions: " + str(oct(stats.st_mode)[-3:]) + "\n"
            newContent += "-+-+-+-+-+-+-+-+\n"


newContent += '-----------------------------------\n'

#3------------------------------
pswdfile = open('/etc/passwd', 'r')

for x in pswdfile:
    if(x.startswith('bin')):
        newContent += x

dir = os.path.dirname(os.path.realpath(__file__))

filepath = dir + '/' + raw_input("Enter filename: ")

if(os.path.exists(filepath)):
    print('Overwriting file ' + filepath)
    with open(filepath, 'w') as f:
        f.write(newContent)
else:
    with open(filepath, 'w+') as nf:
        nf.write(newContent)
        nf.close()
        print("Done! Check result in the file : " + filepath)
