# This script changes the default dns server settings on rpi to Google's DNS servers
# This has to be done because the raspbian buster version experiences domain name server resolution issues with the default DNS servers

def a():
    import os   # importing the os module to work with shell

    # we need to open the dhcp configuration file and specify the dns server details so that when it dynamically generates the resolv.conf(file specifying dns servers) it incorporates the latest dns server information
    # one known issue that the current version of python on raspbian buster does not support the latest python interpreter, so, we need to remove the encoding syntax from open command
    with open('/etc/dhcpcd.conf', 'a', encoding='utf-8') as f:
        f.write('static domain_name_servers=8.8.4.4 8.8.8.8')

    # restarting the dhcpcd server to generate the new resolv.conf file
    os.system('sudo service dhcpcd restart')

    # checking if the correct DNS server settings have been loaded

    with open('/etc/resolv.conf', 'r', encoding='utf-8') as f:
        if '8.8.4.4' and '8.8.8.8' in f.read():
            print('DNS settings successfuly done')
        else:
            print('DNS settings not configured correctly')