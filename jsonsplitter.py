import json 

file_name = "sample.json"
file = open(file_name)
folder = file_name.split(".json")[0]
data = json.load(file)

for k in data["result"]:
    json_name = folder + "/"+ k.get("file_name").split(".pdf")[0]+".json"
    with open(json_name, "w") as write_file:
        json.dump(k, write_file, indent=4)