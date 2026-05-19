# write a program to define and check x ,y and z with is and is not
x = ["Maruti","BMW"]
y = ["Maruti","BMW"]
z = x

print( x is y)
print( z is x)

print( x is not y)
print( z is not x)


#membership operator
y = ["Maruti","BMW"]
x = "Maruti"
print( x in y)