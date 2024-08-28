# os mocule use to create file, delet file, remove file and all of the operation you perfom in you pc infact you are create automaic program using this module

import os

if (not os.path.exists("folder")): # it is check folder is make or not
    os.mkdir("folder") # create new folder
    
os.rename("folder","OS module") 

folders = os.listdir("python") # it is count the folders
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))


# os system method, getcwd, chdi