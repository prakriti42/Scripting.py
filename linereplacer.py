import re
import os 

main_dir = "path_to_parent_dir"
txt_files = os.listdir(main_dir)
new_dir_name = main_dir.split("/")[-1]+"formatted"
if not os.path.exists(new_dir_name):
    os.mkdir(new_dir_name) 
    
for file in txt_files:
    file_reader = open(main_dir+"/"+file,"r")
    file_text = file_reader.read()
    updated_text = re.sub('\n', ' ',file_text)
    updated_text = re.sub(' +', ' ', updated_text)
    if not updated_text:
        print("Empty data found")
        print(file)
        continue 
    file_writer=open(new_dir_name+"/"+file,"w")
    file_writer.write(updated_text)
    

print("Cleaned all the data file and stored to " + new_dir_name)