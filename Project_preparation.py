import os
from github import Github

print(' ')
print("  ***   Welome in project creation tool  ***  ")
print(' ')


project_name = input( '   Please provide project name which should be created: ')
print(' ')

# Creation of folder on drive
os.system("mkdir C:\\Download\\Development\\" + project_name)
print(' *  1/3 Folder was created for new project')
print(' ')


# Creation of repo on Github
g = Github(' ea7f1cd79798a1245290ea37d372990a5f895799')

user = g.get_user()
repo = user.create_repo(project_name)
 
print(' *  2/3 Remote repository was created on Github')
print(' ')

# Cloning og repo from Github
os.system("cd C:\\Download\\Development\\" + project_name)
os.system("git clone https://github.com/Pr00bit/"+project_name+".git")

print(' ')
print(' *  3/3 Remote repository was cloned to local directory')
print(' ')