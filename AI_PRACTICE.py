import numpy as np

# arr_1 = np.array([1,2,3])
# print(arr_1)

# a1 = np.array([[1,2,3], [1,2,3]])
# a2 = np.array([[1,2,3], [1,2,3]])

# print(a1*a2)


# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# scalar = 10
# print(arr + scalar)

# row_vector = np.array([1, 2, 3])
# print(arr + row_vector)

# col_vector = np.array([[1], [2], [3]])
# print(arr + col_vector)

# A = np.array([[1,2], [2,2]])
# B = np.array([[5, 6], [7, 8]])
# print(np.dot(A,B)) #multiplication of two matrix

# print(A.T)

# print(np.linalg.inv(A))   #inverse of matrix A

# angles = np.array([0, 30, 45, 60, 90]) * np.pi / 180  # radians convert
# print("Sin:", np.sin(angles))
# print("Cos:", np.cos(angles))

# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("Sum:", np.sum(data))
# print("Sum along rows:", np.sum(data, axis=1))
# print("Sum along columns:", np.sum(data, axis=0))
# print("Min:", np.min(data))
# print("Max:", np.max(data))
# print("Std deviation:", np.std(data))

# a  = np.random.rand(3,3) #generate random matrix from 0 to 1 in 3X3
# print(a)

# a = np.random.randint(1, 100, 10)
# print(a)

# a = np.random.seed(41)  #generate fix value each time a code will run.
# print("With seed 41:", np.random.rand(3))

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# np.save('my_array.npy', arr)

# load_array = np.load('my_array.npy')
# print(load_array)

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# #(Boolean indexing)
# bool_mask = arr > 5
# print("Elements > 5:\n", arr[bool_mask])

# # (Fancy indexing) - integer arrays से index करना
# rows = np.array([0, 2])
# cols = np.array([1, 3])
# print("Selected elements:", arr[rows, cols])

# # व्हेयर (where) कंडीशन
# condition = arr > 7
# result = np.where(condition, arr, -1)  # condition true तो arr value, false तो -1
# print("Where condition:\n", result)

#PROGRAM TO CONVERT CLECIUS TO FAHRENHEIT 

# celsius = np.array([22, 25, 19, 30, 28, 24, 20])
# fahrenheit = (celsius * 9/5) + 32

# print(celsius) #Celsius 
# print(fahrenheit) #Fahrenheit
# print(np.mean(celsius)) #Average temperature:
# print(np.max(celsius))  #Hottest day

# Generate random number between 1 and 50


# Python list
# guesses = [5, 10, 15, 20]
# print(guesses * 2)  # [5, 10, 15, 20, 5, 10, 15, 20] (repeat karta hai)

# NumPy array
# guesses_np = np.array([5, 10, 15, 20])
# print(guesses_np * 2)  # [10, 20, 30, 40] (har element multiply)


# Game mein ye line:
# np.abs(np.array(guesses) - secret)
# Example:
# guesses = np.array([10, 25, 40, 15])
# secret = 20
# result = guesses - secret  # [10-20, 25-20, 40-20, 15-20] = [-10, 5, 20, -5]

# 2D array banate hain
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(np.mean(matrix, axis=0))  # Har column ka mean: [4, 5, 6]
print(np.mean(matrix, axis=1))  # Har row ka mean: [2, 5, 8]
print(np.mean(matrix))          # Overall mean: 5