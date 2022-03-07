import shutil
import os

# Absolute path of a file
folder = "path"

#Make sure the folder is precreated 
Outputfolder = "path"    

src = os.listdir(folder)

i = 0


#Renaming the file
for file in src: 
    oldfile = f"{folder}/{file}"
    newfile = f"Folder/{i}.png"
    print(oldfile, newfile)
    i = i + 1
    shutil.copyfile(oldfile, newfile)
    print('Renaming.....')

    
print('Renaming complete sucessfully !!') 
