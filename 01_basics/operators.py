# A Operator is a symbol that performs a certain operation on operands 
print("1_arithmetic operator")
# 1) Arithmetic operator (+,-,*,/,%,**)--> these are the operators used for calculations
a=10
b=3
name = "bhanu"
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)  # //--> floor division(it gives the floor of the division result)
print(a%b)  # % --> it gives the remainder after the division
print(a**b)  # ** --> it means raise to the power 


print("2_assignment operator")
# 2) assignment operaor ( =,+= ,-=,) -->used to assign value to the variable
x=10  # = --> is assignment operator 
x+=3
print(x)
x-=4
print(x)
x*=3
print(x)
x/=4
print(x)
x//=2
print(x)
x%=2
print(x)

print("3_comparision operator")
#comparison operator :it compares two values and gives wheteher it is True or False
print(a==10)
print(a!=10)
print(a>11)
print(a<11)
print(a<10)
print(a>10)
print(a>=10)
print(a<=10)

print("4-logic operators")
#logic operators :they allow us to combine conditions (they become important when we use if ,else )
print(a>5 and b>0)
print(a>10 and b>3)
print(a>10 or b>3)
print(a>5 or b>3)
print(not a)

print("5_membership operators")
#membership operators :these operators check wheather something exists inside another object such as strings or lists(in ,not )
print("b" in name)
print("k" in name)
print("k" not in name)

print("6_identity operators")
#identity operators : they check whether two varibles refer to the same object rather than just"whther their values are equal"(is ,is not)
print(a is 10)
print(b is 4)
print(b is not 4)

print("7_ bitwise operator")
#bitwise operartor: these operate on individual bits of numbers(&,^,~,<<,>>)
print(a&b)