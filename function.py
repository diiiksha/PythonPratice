# def message():
#     print("enter a value:")

# message() #invocation/calling a function
# a = int(input())

# message() #invocation/calling a function
# b = int(input())

# message() #invocation/calling a function
# c = int(input())

#
# def message(): #definee...
#     print("enter a value:")

# # message = 1 

# print("we start here.")
# print(message)
# message() #calling
# print("we end here.")

#return the value:-----
# def message():
#     print("enter a value:")
#     temp = int(input())
#     return temp

# print("step1")
# a=message() #invocation/calling a function

# print("step2")
# b=message() #invocation/calling a function

# print("step2")
# c=message() #invocation/calling a function

# print("a:",a)
# print("b:",b)
# print("c:",c)
# def hi():
#     print("hi")
# hi(5)

# def hello(n): #defining a function
#     print("Hello,",n) #body of the function

# name = input("Enter your name:")
# hello(name) #calling the function

# def message(number):
#     print("enter a number:",number)

# number = 1234
# message(1)
# print(number)

# def message(what,number):
#     print("Enter",what,"number",number)

# message("telephone",11)
# message("price",5)
# message("number","number")

#arguments fucntion
# def introduction(first_name,last_name):
#     print("Hello, my name is",first_name,last_name)

# introduction("luke","skywalker")
# introduction("jesse","quick")
# introduction("james","bond")

#keyword arguments
# def introduction(first_name,last_name):
#     print("Hello, my name is",first_name,last_name)

# introduction(first_name="luke",last_name="skywalker")
# introduction(first_name="jesse",last_name="quick")

# def adding(a,b,c):
#     print(a,"+",b,"+",c,"=",a+b+c)

# adding(1,2,3)
# adding(c=1,a=2,b=3)
# adding(3,c=1,b=2)
# adding(3,a=1,b=2) # error multiple value of a

# def happy_new_year(wishes= True):
#     print("Three...")
#     print("two...")
#     print("one...")
#     if not wishes:
#         return
#     print("happy new year!")
# happy_new_year()
# happy_new_year(False)

# def boring_function():
#     print("'Boredom mode' ON.")
#     return 123

# print("the lesson is intersting!")
# boring_function()
# print("This lesson is boring...")

# def checkMYvar(variable):
#     if(variable==10):
#         print("variable is 10")
#         return 2
#     else:
#         print("variable is not up to the mark")
#         return
# checkMYvar(5)
# print()

#LIST PLUS FUNCTION
# def list_sum(lst):
#     s=0

#     for elem in lst:
#         s+= elem

#     return s
# print(list_sum([5,4,3]))
# print(list_sum(2)) # error not iteratable

def strange_list_fun(n):
    strange_list = []

    for i in range(0,n):
        # strange_list.insert(0,i+1)
        strange_list.append(i+1)

    return strange_list

print(strange_list_fun(5))