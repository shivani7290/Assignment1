# Assignment(8):-
#--------------------------------------------------------------
#Question 1:- Create a Numpy array
# - Array with random values
import numpy as np
array= np.random.rand(3, 3)
print("Random array (3x3):\n",array)
# - Empty and full array (4x2)
empty_array = np.empty((4, 2))
full_array = np.full((4, 2), 7)
print("\n Empty array (4x2):\n",empty_array)
print(" Full array (4x2):", full_array)
print('\n')
# - Array filled with zeros (3x5)
zeros_array = np.zeros((3, 5))
print("Zeros array (3x5):", zeros_array)
print('\n')
# - Array filled with ones (4x3x2)
ones_array = np.ones((4, 3, 2))
print(" Ones array (4x3x2):", ones_array)
print('\n')
#---------------------------------------------------------
# Question 2:- Create 3x3 matrix with values from 2 to 10
#---------------------------------------------------------

matrix = np.arange(2, 11).reshape(3, 3)
print(" Matrix 3x3 from 2 to 10:", matrix)
print('\n')
#---------------------------------------------------------
# 3. Null vector of size 10 and set 6th value to 11
#---------------------------------------------------------
vec = np.zeros(10)
vec[5] = 11
print("Null vector with 6th value = 11:",vec)
print('\n')
#---------------------------------------------------------
# Question4:- Reverse an array
#---------------------------------------------------------
arr = np.array([10, 20, 30, 40, 50])
reversed_arr = arr[::-1]
print("Reversed array:", reversed_arr)
print('\n')
#---------------------------------------------------------
# 5. Convert array to float type
#---------------------------------------------------------
array = np.array([1, 2, 3, 4], dtype=float)
print("Float array:", array)
print('\n')
