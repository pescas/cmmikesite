import os 
from shutil import copyfile


for file in os.listdir("."):
    if file.endswith(".jpg"):
        if "large" not in file and "thumb" not in file:
            filenumber = file[:-4]
            if int(filenumber) > 166:
                print file
                #os.remove(file)
            #copyfile(file, str(int(file[5:8])+1)+".jpg")
