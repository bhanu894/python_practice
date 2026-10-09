#dictionaries: a dictionaries stores the information as key and value ,every value has a key
student = {
    "name": "Bhanu",
    "age": 21,
    "branch": "ECE"
}

print(student["name"])
print(student["branch"])

#Dictionary vs List
#List       → index → value
#Dictionary → key   → value

#adding new key to dictionary
student["college"]="pes"
print(student["college"])
print(student)

#dictionaries are mutable
student["age"]=22
print(student["age"])

#removing an item 
student.pop("college")
print(student)

#checking wheather a key exists in the dictionary
print("name" in student)
print("salary"in student)

#getting all keys 
print(student.keys())

#getting all values
print(student.values())

#getting key-value pairs 
print(student.items())

for key in student:
    print(key)

for value in student.values():
    print(value)

for key,value in student.items():
    print(key, ':',value)

student["marks"]=(12,23,34,56,67)
print(student["marks"][0])

#dictionaries inside dictionaries
students = {
    "student1": {
        "name": "Bhanu",
        "age": 21
    },

    "student2": {
        "name": "Rahul",
        "age": 22
    }
}
print(students["student1"]["name"])
print(students["student2"]["age"])