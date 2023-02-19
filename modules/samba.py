# Script to install and setup samba
def f():
    import os   # importing of OS module
    drives = ['1TB', '4TB', '4TB_1']
    path = '/media'
    line_item=[]
    os.system('sudo apt-get install -y samba -y samba-common-bin')

    with open('/etc/samba/smb.conf','a',encoding='utf-8') as f:
        for i in range(len(drives)):
            line = '''
[{}]
path = {}
writeable = Yes
create mask = 0777
directory mask = 0777
public = yes            
            '''.format(drives[i],os.path.join(path,drives[i]))
            line_item.append(line)
            f.write(line)
            os.system('sudo smbpasswd -a pi')
            os.system('sudo systemctl restart smbd')