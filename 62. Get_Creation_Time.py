# 62. Write a Python program to get file creation and modification date/times.

import os.path, time

file_name = 'Resume.pdf'
print("Last modified: %s" % time.ctime(os.path.getmtime(file_name)))
print("Created: %s" % time.ctime(os.path.getctime(file_name)))