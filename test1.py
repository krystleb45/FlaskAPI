from mock_data import mock_data

#Dictionary

me = {
    "name": "Krystle",
    "last": "Berry",
    "age": 35,
    "hobbies": [],
    "address": {
        "street": "Old Cropps",
        "City": "Fredericksburg"
    }
}

print(me["name"])

#print full name
print(me["name"] + " " + me["last"])

#print city
print(me["address"]["City"])

#modify existing
me["age"] = 34

#create new 
me["new"]=1
print(me)



#list

names = []

names.append("ondra")
names.append("elijah")
names.append("kai")

print(names)

#get elements
print(names[0])
print(names[2])

#for loop
for x in names:
    print(x)

ages = [12,32,456,10,23,678,4356,2,46,789,23,67,13]
# 1 youngest
#create a variable with the first (or any) bumber from the list
#travel the list and compare each number with your variable
#if find a younger, update your variable to be that number
#print the variable

youngest = ages[-1]
for age in ages:
    if age < youngest:
        youngest = age

print (youngest)

for item in mock_data:
    print(item["title"])