#conditional statement:a condition is something that results in True or False
age=20
if age>=18:
    print("you are an adult")#note:there are spaces before print ,these are indentation .Python uses indentation to know which code belongs to the if.
else :
    print("you are minor")


marks = 39
if marks>=85:
    print("A")
elif marks>=70:
    print("B")
elif marks>=40:
    print("C")
else :
    print("fail")

if age>= 18 and marks>=60 :
    print("you are eligible")
else:
    print ("not eligible")

permission = False
if age>=18 or permission:
    print("allowed")
else :
    print("not allowed")

#nested loops : using condition statements in a condition statement
if age >= 18:
    if permission:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")


number= 0
if number % 2 == 0:
    print("even")
else :
    print("odd")

if number >0:
    print("positive ")
elif number <0:
    print(" negative")
else:
    print("zero")

name = "bhanu"
if name == "bhanu":
    print("welcome user")
else :
    print("invalid user")

#q1.Write a program that checks whether a person can vote
age = 5
if age < 18:
    print("you are not eligile to vote")
else :
    print("you are eligible to vote")