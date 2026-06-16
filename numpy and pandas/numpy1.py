
import numpy as np

# arr1d = np.array([1,2,3,4,5])
# arr2d = np.array([[85,90,75],[76,78,79],[34,56,79]])

# print(arr2d.shape)
# print(arr2d.dtype)
# print(arr2d.ndim)

# zeros = np.zeros((3,4)) #3x4 array of 0s
# print(zeros)

# ones = np.ones((2,5)) #2x5 array of 1s
# print(ones)

# rng = np.arange(0,50,5) #print the array with the diff of 5
# print(rng)

# lin = np.linspace(0,1,11) #evenly divide the space betwwen 0 to 1
# print(lin)

# random = np.random.randint(40,100,(5,3)) #ramdomly pick the numbers in bet..40 to 100
# print(random)

# arr = np.array([10,20,30,40,50])

# print(arr * 2)
# print(arr +5)
# print(arr ** 2)

# marks_2d = np.array([[85,90,78],[73,88,95],[91,76,83]])

# print(np.mean(marks_2d))  #overall mean
# print(np.mean(marks_2d,axis = 1))  #mean per studednt(row)
# print(np.mean(marks_2d,axis = 0))  #mean per subject(column)
# print(np.max(marks_2d))  #highest number 
# print(np.std(marks_2d)) #standard devaiation

arr = np.array([55,82,43,91,67,78,35,88])
print(arr[arr>70])