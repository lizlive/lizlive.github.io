import os
import sys
import time

title = "uname_file"
ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

file_name = "{}.md".format(title)
path= os.getcwd()
temp = str.split(path,"\\")
categories = temp[-1]

# os.mknod(file_name)
with open(file_name, "w") as fp:
    fp.writelines("---\n")
    fp.writelines("title: {}\n".format(title))
    fp.writelines("date: {}\n".format(ticks))
    fp.writelines("categories: {}\n".format(categories))
    fp.writelines("---\n")