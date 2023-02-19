# Script to perform all the necessary updating on raspbian os

def b():
    import os   # importing the os module to work with shell

    # check for available updates
    os.system('sudo apt-get update')

    # install all the necessary updates with -y modifier to assume yes for all prompts
    os.system('sudo apt-get -y upgrade')