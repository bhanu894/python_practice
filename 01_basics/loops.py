#loops : they are used to run a particular part of the code multiple times 
for i in range(5):
    print("hello")
    print(i)

for v in range(3,9):  #range(start, stop)
    print(v)


for x in range(1,10,2): #range(start, stop,step)
    print(x)

for y in range(10,1 ,-1):
    print(y)

#print odd numbers from 1 -25
print("print odd numbers from 1 -25")
for  a in range(1,25):
    if a % 2 !=0:
        print(a)

name = "bhanu"
for letter in name:
    print(letter)

marks = [1,2,34,56,78]
for mark in marks:
    print(mark)

#while loop: keep repeating the loop until while is true
t = 1
while t<=10:
    print(t)
    t += 1

#note: 1)Use for when you know what you're iterating over(like when you know how many the loop has to run)
#       2)Use while when the loop depends on a condition(like the loop has to be repeated till certain condition is met)

#break :it is used to stop a loop immediately
for i in range(1, 10):
    if i == 5:
        break#as soon as i becomes 5 it comes out of the loop 

    print(i)

#continue :it skips the current iteration and jumps to the next one
for i in range(1,10):
    if i==4:
        continue #when i became 4 ,it skipped that iteration and jumbed to next iteration
    print(i)

#pass : pass means to "do nothing"(it is useful when we want to write a block of code but havent written its contents yet )
for i in range (1,100):
    pass

#nested loops:a looop inside another loop is called nested loop
n=0
for i in range(3):
    for j in range (2):
        print( i , j)  #The inner loop runs completely for each iteration of the outer loop

#print a table 
for i in range (1,11):
    print( "5 x " ,i, "=", 5*i)

total = 0
for i in range (1,101):
    total= total + i

print(total)

#Use a while loop to print

i=0
while i<6:
    print(i)
    i +=1

#Print numbers from 1 to 20, but stop when the number reaches 13 using break
for i in range(1,21):
    if i==13:
        break 
    print(i)

