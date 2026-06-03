#list comprehension

# row = []
# for i in range(8):
#     row.append("WHITE_PAWN")

# row = ["WHITE_PAWN" for i in range(8)]
# print(row)

# squares = [index **2 for index in range(1,11)]
# odds = [f'{element}  Is odd number !' for element in squares if element % 2 !=0]
# print(odds)

#MY PRACTICE QUE----
# Create list of numbers from 1 to 10.
# numbers = [ i for i in range(1,11)]
# print(numbers)

# Convert all names into lowercase
# names = ["DIKSHA","SAKSHI","BITTU"]
# lower_case = [name.lower() for name in names]
# print(lower_case)

# Create list of even numbers from 1 to 20.
# number = [ i for i in range(1,21) if i% 2 == 0]
# print(number)

# Create list of cubes.
number = [ i**3 for i in range(1,21) ]
print(number)