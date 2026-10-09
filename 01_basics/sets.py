#Set : a set stores a unique values,it does not allow duplicate values
set1 = {12,23,4,5,12}#12 is repeated 
print(set1)
names={"bhanu","bhanupra","bhanu","bhanuprakash"}
print(names)

#sets are unordered ,therefore the elements of the sets cannot be accessed by index

#add and remove
set1.add(90)
print(set1)
set1.remove(12)
print(set1)

#set  operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
#union(|) :elements from both the sets

print(A|B)

#intersection(&):elements common to both sets
print(A&B)

#subtraction
print(A-B)
print(B-A)