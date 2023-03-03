# 68. Write a Python program to sort files by date.

import glob
import os

# files = glob.glob("*.txt")
# print(files)
# files.sort(key=os.path.getmtime)
# print(files)
# print("\n".join(files))

import os
os.chdir('C:/Users/LENOVO/Desktop/')
result = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)
print('\n'.join(map(str, result)))