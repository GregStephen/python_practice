f = open('practice.txt', 'w+')
f.write('This is a test string')
f.close()

import os

os.getcwd() #shows current directory

print(os.listdir())

import shutil
# Moves the file!
shutil.move('practice.txt', 'C:\\Users\\Greg\\source')

# os.unlink(path) deletes a file at the path you provide
# os.rmdir(path) deletes a folder (folder must be empty) at the path you privde
# shutil.rmtree(path) this will remove all files and folders contained in the path

# Safe way to delete
import send2trash

shutil.move('C:\\Users\\Greg\\source\\practice.txt', os.getcwd())

send2trash.send2trash('practice.txt')

for folder, sub_folders, files in os.walk(os.getcwd()):
  print(f"Currently looking at {folder}")
  print('\n')
  print('The subfolders are: ')
  for sub_fold in sub_folders:
    print(f"Subfolder: {sub_fold}")

  print('\n')
  print("the files are: ")
  for f in files:
      print(f"File: {f}")