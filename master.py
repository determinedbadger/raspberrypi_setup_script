# Master file to run all the subroutines

#Folders where drive mount points to be specified
Folders = []

#Drive UUIDs to identify them
UUIDs = []

# DNS Server settings
import modules.dns_server as dns_server
dns_server.a()

# UPDATING python's operating system
import modules.updating as updating
updating.b()

# DIRECTORY creation
import  modules.directory as directory
directory.d(Folders,UUIDs)

# SAMBA configuration
import modules.samba as samba
samba.f()

# DELUGE configuration
import modules.deluge as deluge
deluge.g()