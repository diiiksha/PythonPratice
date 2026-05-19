# number = []# decalaration
# print(number)
# print(type(number))

# number = [1,5,6,7,8]
# print(number)
# print(type(number))

# print("first elEment content :",number[0])
# print("second elEment content :",number[1])
# print("third elEment content :",number[2])
# print("fourth elEment content :",number[3])
# print("fifth elEment content :",number[4])


# #updating List
# number[0] = 111
# print("number[0]",number[0])
# print(number)

# #first comvine to fifth
# number[1] = number[4]
# print(number) 
# print(len(number))# length

# del number[3]# deleting an element
# print(number) 
# print(len(number))
# print(number[-1])
# print(number[-2])
# print(number[-3])
# print(number[-4])
# #print(number[-5])
# print(number[4])

#pratice que

# num = [1,3,4,5,6]
# print(len(num))
# del num[-1]
# print(num)

# number = int(input("enter the number:"))
# num[int(len(num/2))] = number
# print(num)

#list method
# list = [5,3,4,2,8]
# list.append(6)
# print(list)

# list.insert(3,10)
# print(list)

# #traversing (dynamically)

# my_list = [1,2,3,4,5,6,7,8,9,10]
# for iterator in range(len(my_list)):
#     print(my_list[iterator])

# list=[]
# for iterator in range(1,11):
#     list.append(iterator)

# print(list)

# list=[]
# for iterator in range(10):
#     list.append(iterator+1)
    
# print(list)


#adding+1
# list = [10,20,30,40,50,60,70,80,90,100]

# for index in range(len(list)):
#     list[index] +=1    #list[index] = list[index]+1

# print(list)


# #sum of all elements without range
# #another version
# list = [10,20,30,40,50,60,70,80,90,100]
# sum = 0
# for i in list:
#     sum += i

# print(sum)

#swaping aur coping the value
variable1 = 1
variable2 = 2

print("variable1 =" , variable1)
print("variable2 =" , variable2)

variable1,variable2 = variable2,variable1
print("variable1 =" , variable1)
print("variable2 =" , variable2)

list = [10,20,30,40,50,60,70,80,90,100]

list[4],list[1] = list[1],list[4]
print(list)