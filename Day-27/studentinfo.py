import json
'''with open("data.json",'r') as file:
    data = json.load(file)
print(data.load)

data["username"]= "Chandu"
data["skills"]="flask"

with open ("data.json",'w') as file:
    json.dump(data,file,indent=4)'''

#dump -  converting data dict to json
#load - converting json to dict 

student = {
    "name" : "Likitha",
    "age" : 23,
    "course" : "Python"
}   

json_data = json.dumps(student)
print(json_data)

student = json.loads(json_data)
print(student)
print(type(student))

