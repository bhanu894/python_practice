#lists: a list is used to store multiple values in a single variable
name = "bhanu"
marks =[23,45,67,89]
marks2 =[12,23,34,45,5,6]
print(marks[0])

#a list doesnt have to contain only numbers
data = ["bhanu",34,67.7,0.55,True]
print(type(data))

#nested list:list inside a list
data2 = ["bhanu",34,45.5,["prakash",89]]
print(len(data2))

marks[2] #==>lists are mutable
print(marks)

#append --> used to add an itrm at the end of the list
marks.append(90)
print(marks)

#insert--> used to add an item at desired position 
#syntax: list.insert(index, value)
marks.insert(0,44)
print(marks)

#remove()-->used to remove a specific value
marks.remove(89)
print(marks)

#pop():used to remove an element using index
marks.pop(2)
print(marks)
marks.pop(2)
print(marks)

#clear()-->clearing the entire list
marks.clear()
print(marks)

marks.append(2)
marks.append(56)
marks.append(34)
marks.append(322)
print(marks)
print(2 in marks)
print(31 in marks)

for i in marks:
    print(i)

for i in marks:
    if i>= 55:
        print(i)


#min() : used to find the smallest value in the list
print(min(marks))

#max() :used to find the largest value in the list
print(max(marks))

#sort() : used to sort the list
print(marks)
marks.sort()
print(marks)

#reverse: reversing a list
marks.reverse()
print(marks)
print(marks[::-1])

#slicing :slicing a list 
print(marks[0:3])
print(marks[:3])

#combinig a list
c=marks+marks2
print(c)

#repeating a list
print(marks*3)

print(len(c))

fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)

for i in marks:
    print(i)

for k in c:
    if k%2==0:
        print(k)

print(sum(c))

for n in c:
    if n>=50:
        print(n)