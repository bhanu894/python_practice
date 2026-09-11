#strings: a string is a sequence of characters
name= "bhanu" 
name2 = 'prakash'
age = 21
#strings can be written in "" and ' ' .Both are valid
number1 = 124
number2 = '124'#even it is numbers but because it is in '' it is string
print(type(number1))
print(type(number2))

#indexing : accessing characters ,python gives each character a position called indexing .python uses zero-based indexing 
print(name[0])#  b  from "bhanu " is in 0th position
print(name[-1]) # negative indexing ,sometimes used to identify the last character

#string slicing :taking a part of string
#syntax : string[start : stop]
print(name[0:4])

#slicing with a step -> string[start:stop:step]
print(name[0:5:2])

#reversing a string 
print(name[::-1]) #-1 tells pyhton to move backwards

#strirng concatination:stirng can be added using +
full_name = name+name2
print(full_name)

#repeating strings *
print(name*2)
print('_'*50)


#stirng methods
#string length:len() tells how many characters are there in string
print(len(full_name))


print(name.upper())
print(name.capitalize())
print(name)
print(name.title())
print(full_name.title())
name3= "  alas   "
print(name3)
print(name3.strip())# strip is used to remove spaces
#string replacement: syntax .replace("old", "new")
message = "i like python"
print(message)
message2=message.replace("python","c")
print(message2)

#splitting strings and joining
fruits = "apple ,orange ,banana"
print(fruits.split(",")) #notice how the string becomes a list
result = ",".join(fruits)
print(result)
fruits2 = ['apple','orange','banana']
result2 = ",".join(fruits2)
print(result2)

#f-string
print(f"my name is {name}{name2} and i am {age} years old")

for letter in name:
    print(letter)

for letter in name:
    if letter == "a":
        print("found a")

print("a" in name)

#Exercise 1:name = "Bhanu",print first and last letter and len of the name 
print(name)
print(name[0])
print(name[-1])
print(len(name))

#exercise2 :name = "python " .print p and o
name4 = "python"
print(name4[0:10:4])

message4 ="hello world"
print(message4[0:5])
print(message4[6:11])

print(name4[::-1])
branch = "ECE"

print(f"my name is {name}{name2} , i am {age} years old , i am from {branch}")