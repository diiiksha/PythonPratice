print(5 >> 2) #bitwise operator

#colon operator

print(x:=3)

#comparison opertor 
x=1
print(x==1)
print(x==2)

x=4
print(x < 5 and x < 10)
print(x > 5 or x > 10)
print(x > 3 or x > 10)
print(not(x > 3 or x > 10))

#identity opwertor
x = 10
y = 20
print( x is y)

x = 10
y = 10
print( x is y)

# name = input("enter your name:")
# print("hello",name)


#input string concatenation 
x = input("enter first value for sum:")
y = input("enter first value for sum:")
z = x+y
print("sum:",z) #joining two string 

z = int(x)+int(y)  # type casting
print("sum:",z)