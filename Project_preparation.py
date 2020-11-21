import os
from github import Github

print(' ')
print("  ***   Welome in project creation tool  ***  ")
print(' ')


project_name = input('Please provide project name which should be created: ')

# Creation of folder on drive
os.system("mkdir C:\\Download\\Development\\" + project_name)
print(' * Folder was created for new project')
print(' ')


# Creation of repo on Github
g = Github('a5810f363d5c985a7a27e01133bea2f830e8610a')
user = g.get_user()
repo = user.create_repo(project_name)

print(' * Remote repository was created on Github')
