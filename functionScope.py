def scope_test():
    x=123  # local variable
scope_test()
# print(x)

def my_function():
    print("do i know the variable!",var)

var =1  #global variable
my_function()
print(var)

def mult(x):
    var=7
    return x*var
var = 3
print(mult(7))

def  my_function():
    global var #global keyword
    var=2
    print("do i know that variable?",var)

var = 1
my_function()
print(var)

var = 2
print(var) #ouput:2

def return_var():
    global var 
    var = 5
    return var
print(return_var())
print(var)

def my_function(n):
    print("i got",n)
    n+=1

    print("i have",n)
var = 1
my_function(var)
print(var)

def my_function(my_list_1):
    print("print #1",my_list_1)
    print("print #2",my_list_2)
    my_list_1 = [0,1]
    print("print #3:",my_list_1)
    print("print #4:",my_list_2)

my_list_2 = [2,3]
my_function(my_list_2)
print("print #5:",my_list_2)

def my_function(my_list_1):
    print("print #1",my_list_1)
    print("print #2",my_list_2)
    del my_list_1[0]
    print("print #3:",my_list_1)
    print("print #4:",my_list_2)

my_list_2 = [2,3]
my_function(my_list_2)
print("print #5:",my_list_2)

#recursion
def countDown(number):
    print(number)
    if number == 0:
        return
    else:
        print("going in rec:",number)
        countDown(number-1)
        print("out in rec:",number)

print("staring recursion") 
countDown(5)
print("completed recursion")

#recurion factorial
def factorial(number):

    if number <= 0:
        return 1
    else:
        return number *factorial(number-1)
    
print(factorial(5))




