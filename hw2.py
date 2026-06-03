# rows = 5
# i = 1
# while i<= rows:
#     spaces = " "* (rows - i)
#     star = "*"* (2*i - 1) 

#     print(spaces + star)
#     i +=1

# Write a program to print a series like this:
# 1, 2, 3, 4, 5….50
# # 1, t, 3, t, 5, t, 7, t, 9……50
# # 1, 2, t, 4, 5, t, 7, 8, t…..50
# # 1, 2, fiz, 4, buz, fiz, 7, 8, fiz, buz, 11, fiz, 13, 14, fizbuz, 16……50

# for i in range (1,51):
#     if i % 3 == 0 and i%5==0:
#         print("fizbuz",end=",")
#     elif i % 5 == 0:
#         print("buz",end=",")
#     elif i % 3 == 0:
#         print("fiz",end=",")
#     else :
#         print(i,end=" , ")

# year = int(input("enter the year:"))

# if year < 1582:
#     print("not in the grogeian calender")

# elif year % 4 != 0 and year % 400 != 0 :
#     print("it a common year")

# elif year % 100 !=0:
#     print("it is a leap year")

# else:
#     print("leap year")

# The Mississippi River is about 2,340 miles long, which makes it the second longest river in the United States (the longest being the Missouri River). It's so long that a single drop of water needs 90 days to travel its entire length!
# The word Mississippi is also used for a slightly different purpose: to count mississippily.If you're not familiar with the phrase, we're here to explain to you what it means: it's used to count seconds.
# The idea behind it is that adding the word Mississippi to a number when counting seconds aloud makes them sound closer to clock-time, and therefore "one Mississippi, two Mississippi, three Mississippi" will take approximately an actual three seconds of time! It's often used by children playing hide-and-seek to make sure the seeker does an honest count.

# for i in range(1,6):
#     print(i,"mississipi")

# print("ready or not ,here i come")

# user_word = str(input("enter a word:"))
# user_word = user_word.upper()
# without_vowel =""

# for vowel in user_word:
#     if vowel == "A":
#         continue
#     elif vowel == "I":
#         continue
#     elif vowel == "E":
#         continue
#     elif vowel == "0":
#         continue
#     elif vowel == "U":
#         continue
#     without_vowel+= vowel

# print(without_vowel)

# blocks = int(input("Enter the block:"))
# layer = 1
# height = 0

# while blocks >= layer:
     
#     blocks = blocks - layer
#     layer+=1
#     height+=1
# print("the height of a pyramid",height)

# in 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:
# count = 0
# C0 = 16

# while C0 != 1:
#     if C0 % 2==0:
#         C0 = C0//2
#     else:
#         C0 = 3*C0+1
#     print(C0)
#     count+=1
# print("total count",count)

#LIST QUESTIONS PRACTICE------

# numbers = [1,2,3,4,5]
# print(len(numbers))

# del numbers [4]

# num = int(input("Enter the number:"))
# numbers [len(numbers)//2] = num

# print(numbers)

# beatless = []
# beatless.append("John Lennon")
# beatless.append("Paul Mccartney")
# beatless.append("George harrison")

# for member in ["stu stucifi","pete best"]:
#     name = input("add memeber:")
#     beatless.append(name)

# del beatless[4]
# del beatless[3]
# beatless.insert(0, "ringo starr")

# print(beatless)

# for i in range(1,51):
#     if i % 3 == 0 and i % 5==0:
#         print("fizbuz",end=",")
#     elif i % 5 == 0:
#         print("buzz",end=",")
#     elif i % 3 == 0:
#         print("fiz",end=",")
#     else:
#         print(i,end=",")

# Write a Program to Count Numbers of Digits in this String
# Input: string = "MindCoders password2 is : 1234

# string = "MindCoders password2 is : 1234"
# count = 0
# for ch in string:
#     if ch.isdigit():
#         count+=1
# print("number of count",count)

# Write a Program to Count Numbers of Digits in this String
# Input: string = "U r a a n S 0 f t s k i l l 1 s 1234"

# string = "U r a a n S 0 f t s k i l l 1 s 1234"
# count = 0
# for ch in string:
#     if ch.isdigit():
#         count+=1
# print("total number of count:",count)

# Write a program to find the count for the occurrence of 's' or 'S' character in a string
# Input: "MindCoders"

# string = "MindCoders"
# count = 0
# for ch in string:
#     if ch == "s" or ch=="S":
#         count+=1
# print(count)

# Write a program to count the number of repeated characters and unique characters in a string
# Input: "UraanSoftskills"
# string ="UraanSoftskills"
# repeated = 0
# unique = 0
# for ch in string:
#         if string.count(ch)>1:
#                 repeated+=1 
#         else:
#                 unique+=1
# print("repeated words:",repeated)
# print("unique words:",unique)


#printing 0 to 10 natural number
# for num in range(1,11):
#     print(num)

#print even number
# for num in range(0,11):
#     if num % 2 == 0:
#         print(num)

#sum of all number
# sum = 0
# for num in range(1,16):
#     sum = num + sum
# print(sum)
    
# ⁠Write a program to print a multiplication table of a given number 15

# for i in range(1,11):
#     print("15*",i,"=",i*15)

# 6. Write a program to display numbers from a list using a for the loop [1,2,4,6,88,125]

# list = [1,2,4,6,88,125]
# for elem in list:
#     print(elem)k
 
# 7. ⁠Write a program to count the total number of digits in a number 129475

num = "129475"
count = 0
for elem in num:
    if elem.isdigit():
        count+=1
print(count)

# 8. Write a program to check if the given string is a palindrome - madam
# word = "madam"
# reverse = ""
# for ch in word:
#     reverse = ch + reverse 
# if word == reverse :      
#     print("palidrome ",reverse)
# else:
#      print("not a palidrome")

#reversee the string
# word = input("Enter a word:")
# reverse = ""
# for ch in word:
#     reverse = ch + reverse 
# if reverse == reverse :      
#     print(" reversed :",reverse)


#armstong number

num = int(input("enter a number:"))
original = num
sum = 0 
while num > 0:
    digit = num % 10
    sum = sum + digit**3
    num = num // 10
if sum == original:
    print("armstrong number")
else:
    print("not armstrong")





 