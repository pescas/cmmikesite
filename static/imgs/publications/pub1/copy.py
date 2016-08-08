import os 
from shutil import copyfile


for file in os.listdir("."):
    if file.endswith(".jpg"):
        if file[0:4]=="page":
            print file
            copyfile(file,"normal-" + str(int(file[5:9])+1)+".jpg")
