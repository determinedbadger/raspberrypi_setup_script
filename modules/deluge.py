# Script to setup deluge

# List defining the startup script to add into the 'rc.local' 
startup = ['sudo -u pi /usr/bin/python /usr/bin/deluge-web\n','sudo -u pi /usr/bin/python /usr/bin/deluged\n']

def g():
    # importing various modules
    import os
    import shutil

    # bash commands
    os.system('sudo apt install deluged deluge-web deluge-console python-mako')
    os.system('sudo pkill -i deluged')
    os.system('echo "<USERNAME>:<PASSWORD>:10" >> ~/.config/deluge/auth')
    os.system('deluged')
    os.system('deluge-console "config -s allow_remote True"')
    os.system('deluge-web -f')

    # create a backup copy of 'rc.local'
    shutil.copyfile('/etc/rc.local','/etc/rc.local.tmp')  

    # Store contents of rc.local in a list 'a' for updation
    with open('/etc/rc.local',encoding='utf-8') as f:
        a=f.readlines()
    
    # Find out index of 'exit 0' string in list 'a'. Try and Except block used to handle both cases of 'exit 0' with and without a new line character: \n
    try:
        index = a.index('exit 0\n')
    except:
        index = a.index('exit 0')

    # update the list 'a' with required startup script
    for i in range(len(startup)):
        a.insert(index,startup[i])

    # Write the updated list 'a' into 'rc.local' file
    with open('/etc/rc.local','w',encoding='utf-8') as f:
        f.writelines(a)
