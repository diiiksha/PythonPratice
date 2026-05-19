# while True:
#     print(" i m stuck inside a loop.")


# largest_number = -999999999

# number = int(input("enter the number or type-1 to stop:"))

# while number != -1:
#     if number > largest_number:
#         largest_number = number

#     number = int(input("enter the number or type-1 to stop:"))
       
# print("the largest number",largest_number)


# #print 1 to 50  and how many are even and odd .and it terminates when enter 0
# number = int(input("enter the number:"))

# count = 1
# even = 0
# odd = 0
# while count <= number:
#     if count % 2 == 0:
#         even +=1
   
#     else:
#         odd +=1
#     count +=1
#     if count == 25:
#         count = 51
#         count +=1

# print("Even-",even)
# print("Odd-",odd)

#for loop

# for counter in range(100):
#     print("counter:",counter)

# for counter in range(2,10,2):
#     print("counter:",counter)

# for counter in range(2,10,2):
#     print("counter:",counter)
    
for counter in range(2,1):
    print("counter:",counter)


#power of 2
# power = 1
# for expo in range(16):
#     print(" 2 to the power of ",expo,"is",power)
#     power *= 2

#break and continue
print("the break construction:" )
for counter in range(1,6):
    if counter == 3:
        continue
        # break
    print("insdie the loop",counter)
print("outside the loop")