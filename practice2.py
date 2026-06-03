
# Take a number from user.
# Print "Positive" if number is greater than 0.

# num = int(input("Enter the number:"))

# if num > 0:
#     print("positive")

# Take age as input.
# If age is 18 or above, print "Eligible for vote".

# age = int(input("Enter your age:"))

# if age >= 18 :
#     print("Eligible for vote")

# Take a number from user.
# If number is divisible by 5, print "Divisible by 5"

# num = int(input("Enter the number:"))

# if num % 5 == 0:
#     print("divisible by 5")

# Take a number from user.
# Print "Even" if number is even, otherwise "Odd".

# num = int(input("Enter the number:"))

# if num % 2==0:
#     print("EVEN")
# else:
#     print("ODD")

# Take two numbers from user.
# Print the greater number.

# num1 = int(input("Enter the number1:"))
# num2 = int(input("Enter the number2:"))

# if num1 > num2 :
#     print("number 1 is greater:",num1)
# else :
#     print("number 2 is greater:",num2)

# Create a grading system:

# Marks	Grade
# 90+	A
# 70-89	B
# 40-69	C
# Below 40	Fail

# marks = int(input("Enter the number:"))

# if marks >= 90 :
#     print("Grade A")

# elif marks >= 70 :
#     print("grade B")

# elif marks >= 40 :
#     print("grade B")

# else:
#     print("fail")

# Make a simple calculator using elif.
# operator = input("enter the operator(+,-*,/):")

# num1 = int(input("Enter the number1:"))
# num2 = int(input("Enter the number2:"))

# if operator == "+" :
#     print("add ",num1+num2)

# elif operator == "-" :
#     print("sub",num1-num2)

# elif operator == "*" :
#     print("mul ",num1*num2)


# elif operator == "/" :
#     print("div ",num1/num2)

# else:
#     print("invalid operator")

# Print numbers from 1 to 10.
# Print even numbers from 1 to 20.

# for i in range(1,11):
#     print(i)

# for i in range(0,21,2):
#     print(i)

#creating table of any number
# num = int(input("Enter the number:"))
# for i in range(1,11):
#     print(num*i)

# Find sum of numbers from 1 to 100.

# sum = 0
# for i in range (0,101):
#     sum = sum + i
#     print(i)
# print(sum)

# Print numbers from 1 to 10 using while.

# count = 1
# while count <= 10:
#     print(count)
#     count +=1

# Keep asking password until correct password is entered.

# correct_password = "python123"

# while True:
#     password = input("enter pasowrd:")

#     if password == correct_password:
#         print("login succesfully")
#         break

#     else:
#         print("wriong pasword")


# Find factorial of a number using while.

# num = 5
# count = 1
# factorial = 1

# while count <= num:
#     factorial = factorial * count
#     count += 1

# print(factorial)

# Count how many numbers between 1 and 50 are divisible by 3.
# count = 0

# for i in range(1,51):
#     if i%3 == 0:
#         print(count)
#         count+=1
# print("the numbers of count divisible by 3 is:",count)

#print pattern

# i = 1
# while i <=5:
#     print("*" *i)
#     i +=1

#wheatheer the year is leap year or not
# year = int(input("Enter the year:"))

# if (year % 4 == 0 and year% 100 != 0 or year % 400 == 0):
#     print("leap year")
# else:
#     print("not a leap yeaar")

# Reverse a number.Input: 123 Output: 321
# num = int(input("enter a num:"))
# reverse = 0 
# while num > 0 :
#     digit = num%10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("reverse number:",reverse)

#wap to print palidrome
# num = (input("enter a num:"))
# reverse = 0 
# original = num
# while num > 0 :
#     digit = num%10
#     reverse = reverse * 10 + digit
#     num = num // 10
# print("reverse number:",reverse)
# if original == reverse:
#     print("it is a palidrome")
# else:
#     print("it is not a palidrome")

# AND operatorr(LOGICAL OPERATOR)

# age = 20
# citizen = True

# if age>= 18 and citizen == True :
#     print("eligible for vote")

#not operator
# is_raining = False

# if not is_raining :
#     print("i will go outside")

# & OPERATOR(BITWISE)
# a = 5
# b = 3

# print (a & b)

# checking num in betn..
# num = 56

# if num>0 and num < 100 :
#     print("number is in between 1 & 100 ::",num)

# print( 6 & 4)


# # and or xor que
# a = 1
# b = 0
# c = 1&0
# d = 1|0
# e = 1^0

# print(a+c+d+e)

# #BREAK KEYWORD
# for i in range(1, 11):

#     if i == 5:
#         break
#     print(i)

# #CONTINUE KEYWORD*...
# for i in range(1, 6):

#     if i == 3:
#         continue
#     print(i)

# rows = 5
# i = 1
# while i<= rows:
#     spaces = " "* (rows - i)
#     star = "*"* (2*i - 1) 

#     print(spaces + star)
#     i +=1

# Write a program to print a series like this:
# 1, 2, 3, 4, 5….50
# 1, t, 3, t, 5, t, 7, t, 9……50
# 1, 2, t, 4, 5, t, 7, 8, t…..50
# 1, 2, fiz, 4, buz, fiz, 7, 8, fiz, buz, 11, fiz, 13, 14, fizbuz, 16……50

for i in range (1,51):
    if i % 3 == 0 and i%5==0:
        print("fizbuz",end=",")
    elif i % 5 == 0:
        print("buz",end=",")
    elif i % 3 == 0:
        print("fiz",end=",")
    else :
        print(i,end=" , ")

        
