# prepared by Marcin Idzik (Pr0soft)

import os                                # we import os as we want to be able to use commands to manipulate Operating System
from github import Github                # we import github as we want to use commands to communicate with Github

print(' ')
print("  ***   Welome in project creation tool  ***  ")
print(' ')


project_name = input( '   Please provide project name which should be created: ')   # we ask user to provide name of project 
print(' ')

# Creation of folder on drive
os.system("mkdir C:\\Download\\Development\\" + project_name)         # here we create a folder on a drive which is same as user provided in input
print(' *  1/3 Folder was created for new project !')
print(' ')


# Creation of repo on Github
g = Github(' ')                                    # Here we put token from Github, otherwise there will be error during creation of  repo on Github

user = g.get_user()                                # we get our username
repo = user.create_repo(project_name)              # here we create repo on Github using name provided in input
 
print(' *  2/3 Remote repository was created on Github !')
print(' ')

# Cloning og repo from Github
os.system("cd C:\\Download\\Development\\" + project_name)                # here we go inside directory which was provided in input 
os.system("git clone https://github.com/Pr00bit/"+project_name+".git")    # we clone repository from Github to local drive

print(' ')
print(' *  3/3 Remote repository was cloned to local directory !')
print(' ')

# Activation o"n virtualenv

os.chdir("C:\\Download\\Development\\" + project_name)   # changing directory works better when use chdir not cd
os.system("virtualenv .")                                # installation of virtual environment



print(' ')
print(' *  4/4 virtualenv was instaled for the project !')
print(' ')
