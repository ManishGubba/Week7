import json

 
def rFile():
    with open("baby_names.txt","r") as file:
        new_File = json.load(file) 

    babyDict = {"top":{}} 
    for i in new_File["top"]:
        if i in ("Gary", "Aaron","Luke", "Winston", "Avery"):
            continue
        
        if new_File["top"][i]=='28': 
            continue
        
        elif "v" in i:
            continue
        
        else: 
            babyDict["top"][i]=new_File["top"][i]
    
    babyDict["top"]["Ron"]="5" 
    return babyDict 

def wFile(i):

    with open("better_names.txt", 'w') as file:
        json.dump(i, file, indent = 4) 



i = rFile()
wFile(i)

