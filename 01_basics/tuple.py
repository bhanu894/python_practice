#tuple:a tuple is similar to list the only difference is that tuples are immutable
marks=(12,23,34,45,56,12,12)# this is a tuple
marks2=[12,23,34,45,56]# this is a list
#marks[0]=32  ==> this will give error as tupple is immmutable
marks2[0]=32
print(marks2)
print(marks[1:4])
print(marks)

for i in marks:
    print(i)

#tuple methods:a)count and b)index
print(marks.count(12))#counts how many times the value has repeated in the tuple
print(marks.index(56))# gives the index of the value in the tuple
print(marks.index(12))
