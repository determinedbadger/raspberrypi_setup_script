# Script to create mounting folders and update their mount instructions in the fstab of a linux installation 

def d(folders,UUIDs):
    
    # DIRECTORY CREATION
    # importing os module to process shell commands
    import os

    #Installing ntfs-3g filesystem
    os.system('sudo apt-get install ntfs-3g')

    # List of folders where drives are to be mounted, 
    # Make sure to specify sufficient no. of folders
    folders = []

    # Enter the master directory where the folders are to be created
    path = ''    
    path = '/'+path #adding a suffix of '/' to specify linux directory name
    
    # loop to combine the path and file names required and create their corresponding directories
    for i in range(len(folders)):
        try:
            os.mkdir(os.path.join(path,folders[i]))  # Make directory
            os.chmod(os.path.join(path,folders[i]), mode= 0o777) # Change permissions of the created directory
            print(folders[i], 'created successfully')
        except:
            print(folders[i],'cannot be created')    # Message when directory cannot be created
    
    #DRIVE MOUNT INSTRUCTIONS
    #specify the UUID of your drives as a list with UUID as string elements
    UUID = []
    #check if number of uuid corresponds to the number of mount folders
    if(len(folders!=UUID)){
        print(r"No. of folders provided don't match the number of UUIDs provided!")
    }
    #filesystem to mount with
    file_system='ntfs-3g'
    #drive mount parameters, refer the linux documentation for more info
    mount_parameters = 'auto,exec,rw,async,nouser'
    #an empty list to contain drive mount instructions
    paths = []
    
    with open('/etc/fstab','a',encoding='utf-8') as f:
       for i in range(len(UUID)):
           try:
               directory = 'UUID=' + UUID[i] + '\t' + os.path.join(path,drives[i]) + '\t' + file_system + '\t ' + mount_parameters + '\n'
               paths.append(directory)
               f.write(paths[i])
               print(drives[i],'successfully mounted')
           except:
               print('Failed to setup mount instructions for',drives[i])