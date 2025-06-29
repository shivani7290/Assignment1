#Assignment (9):-
#-----------------------------------------------------------------
# Question 1:-combining a one and a tow-dimensional Numpy array
#----------------------------------------------------------------
import  numpy as np
arr1=np.array([10,20])
arr2=np.array([[1,2],[3,4]])
combine=np.concatenate((arr2, arr1.reshape(1, 2)), axis=0)
print('comined two arrays:\n',combine)
print('\n')
#-----------------------------------------------------------------
#Question 2:- Flatten a 2D numpy array into 1D array
#-----------------------------------------------------------------
import numpy as np
array=np.array([[1,2,3,4],[6,7,8,9]])
flat=array.flatten()
print('flatten array:\n',flat)
print('\n')
#---------------------------------------
#question 3:- Reverse a numpy array
#----------------------------------------
import numpy as np
arr=np.array([[13,20,11],[12,4,9]])
print("array before reverse\n",arr)
reverse=np.flip(arr)
print("array after reversing array:\n",reverse)
print('\n')
#---------------------------------------
#Question 4:- Practice operations
#---------------------------------------
# a) Maximum value
import numpy as np
array=np.array([[10,2,30],[7,20,15]])
print("The maximum value from given array:",array)
print('\n')
# b) Minimum value
print("the minimum value from given array:",array)
print('\n')
# c) the number of rows and columns of a given array using numpy
rows,cols =array.shape
print("Rows:", rows, "| Columns:", cols)
print('\n')
# d) Select the elements from a given array
print("Element at (1, 2):",array[1, 2])
print("\n")
# e) sum of values in a 2d array using for loop
total= 0
for row in array:
    for val in row:
        total += val
print("Sum of all values:", total)
print("\n")
# f) adding,subtracting,multipyling ,dividing array in numpy
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print("\nAddition:", array1 + array2)
print("Subtraction:\n", array1 - array2)
print("Multiplication:\n", array1 * array2)
print("Division:\n", array2 / array1)