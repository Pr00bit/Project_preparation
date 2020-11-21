import os


print(' ')
print("  ***   Welome in project creation tool  ***  ")
print(' ')
project_name = input('Please provide project name which should be created: ')

# Creation of folder on drive
os.system("mkdir C:\\Download\\Development\\" + project_name)
print(' * Folder was created for new project')


