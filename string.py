# city = 'bhopal'
# print(city[0])
# print(city[2])

# print(city[-1])
# print(city[5])

# print(city[-3])
# print(city[3])


# #silcing
# name = "priya sharma"
# print(name[0:5])
# print(name[6:])
# print(name[:5])
# print(name[::5])  #every  2 charca---
# print(name[::-1])

# print(len(city))
# print(len(name))

# #methods

# text = '  Hello Python World!  '

# #case
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize()) # first only capital or small

# #strip whitespace
# print(text.strip())  #remove whitespaces

# #search

# print('Python' in text)    #True

# print(text.find('Python'))  #8(included space)
# print(text.count('l'))

# #replace
# print(text.replace('Python','AI'))

# #split and join
# csv = 'rahul,22,bhopal,engineer'
# parts = csv.split(',')
# print(parts)
# print(parts[0])
# rejoined = ' | '.join(parts)
# print(rejoined)

# #check content
# print('hello123'.isalnum())
# print('12345'.isdigit())
# print('Python'.isalpha())
# print('  '.isspace())

# #start/end check
# email = 'student@gmail.com'
# print(email.endswith('.com'))
# print(email.startswith('stu'))

# # f-string------
# name,marks,rank = 'Anita',92.567,3

# #basic
# print(f'Hello, {name}!')

# #format numbera
# print(f'Marks: {marks:.2f}')
# print(f'Marks: {marks:.0f}')
# print(f'count: {1000000:,}')


# #padding and alignment
# print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')
# print(f'hello {name:^10}')
# print(f'hello {name:>10}')
# print(f'hello {name:<10}')
# print(f'hello {name:*^11}')



# #expression inside {}
# price , gst = 500,0.18
# print(f'Price:Rs.{price}|Gst:Rs.{price*gst:.2f}|Total :rs.{price*(1+gst):.2f}')


# string = "Hello, How are you doing today?"
# #Count vowels in the string
# #print you from the string
# # print the string in reverse order

# print(string[15:18])

# print(string[::-1])

# non_palin,palin = "abcdef","axttxa"
# #check if the string is palidrome or not
# reverse = non_palin[::-1]
# if reverse == non_palin:
#     print("palidrome")
# else:
#     print("not palidrome")

# reverse1 = palin[::-1]
# if reverse1 == palin:
#     print("palidrome")
# else:
#     print("not palidrome")

#file
# with open("data.txt","r") as file:
#     data = file.read()

# print(data)

#creating a file
# with open('students.txt','w') as f:
#     f.write('Rahul Sharma,85,BHopal\n')
#     f.write('priya sharma,86,indore\n')
#     f.write('amit Sharma,87,jabalpur\n')

# with open('students.txt','a') as f:
#     f.write('sneha joshi,38,bhopal\n')

with open('students.txt','r') as f:
    content = f.read()
print(content)


with open('students.txt','r') as f:
    for line in f:
        name,marks,city = line.strip().split(',')
        print(f'{name:<15}|{marks:>5}|{city}')
        print("---------------")