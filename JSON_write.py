import json

data = {}  
data['colour'] = "red"  
data["pieces"] =[]
data["pieces"].append([0,0])
data["pieces"].append([0,-1])
data["pieces"].append([-2,1])
data["blocks"] =[[-1,0],[-1,1],[1,1],[3,-1]]
#data["blocks"].append({[-1,0],[-1,1],[1,1],[3,-1]})

with open('data_1.txt', 'w') as outfile:  
    json.dump(data, outfile)