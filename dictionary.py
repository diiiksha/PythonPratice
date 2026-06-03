# dictionary = {
#     "cat":"chat",
#     "dog":"chien",
#     "horse":"cheval"

# }
# phone_numbers = {'boss':5551234567,'suzy':223456778}
# empty_dictionary = {}

# print(dictionary)
# print(type(dictionary))
# print(phone_numbers)
# print(type(phone_numbers))
# print(empty_dictionary)
# print(type(empty_dictionary))

# print(dictionary['cat'])
# print(phone_numbers['suzy'])
# # print(phone_numbers['presdient'])

# words = ['cat','lion','horse']

# for word in words:
#     if word in dictionary:
#         print(word,"->",dictionary[word])
#     else:
#         print(word,"is not in dictionary")

# print(dictionary.keys())
# for key in dictionary.keys():
#     print(key,"->",dictionary[key])

# print(dictionary.items())

# for key,value in dictionary.items(): #for both print key value item value
#     print(key,"->",value)

# print(dictionary.values())

# for value in dictionary.values():
#     print(value)

# pol_eng_dictionary = {
#     "zamek":"castle",
#     "woda":"water",
#     "galeba":"soil"
# }
# print("pol_eng_dictionary:",pol_eng_dictionary)
# copy_dictionary = pol_eng_dictionary.copy()

# print("copy_dictionary:",copy_dictionary)

# pol_eng_dictionary["zamek"] = "lock"
# item = pol_eng_dictionary["zamek"]
# print(item)
# print(pol_eng_dictionary)

# phonebook = {}
# print(phonebook)
# phonebook["adam"] = 34567898 #create/add a key value pair
# print(phonebook)   #ouputs:{'adam:34566788}

# del phonebook["adam"]
# print(phonebook)

# pol_eng_dictionary = {"kwait":"flower"}

# pol_eng_dictionary.update(
#     {
#         "gleba":"soil"
#     }
# )
# print(pol_eng_dictionary)
# pol_eng_dictionary.popitem()
# print(pol_eng_dictionary)
                      
# pol_eng_dictionary = {
#     "zamek":"castle",
#     "woda":"water",
#     "gleba":"soil"
# }

# if "zamek1" in pol_eng_dictionary:
#     print("Yes!zamek1 is present in the dictionary")
# else:
#     print("no! zamek1 is not prsnet in the dictionary")

# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# del pol_eng_dictionary["zamek"]
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# pol_eng_dictionary.clear()
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# del pol_eng_dictionary
# print(pol_eng_dictionary)

#PRACTICE 
sd = {}

while True:
    name = input("Enter student's name:")
    if name == "":
        break
    score = int(input(f"Enter {name}'s score:"))

    if score not in range(1,11):
        break
    if name in sd:
        sd[name] += (score, )
    else:
        sd[name] = (score, ) 

print(sd)

for name,mark in sd.items():
    sum = 0
    for m in mark:
        sum += m
    print(name,"->",sum/len(mark))

    