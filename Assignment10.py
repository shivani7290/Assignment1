#ASSIGNMENT 10:-
#------------------------------------------------------------------------------------------------------------
#Question(1):- Replace Nan with o and interchange 3 rows and 3 collumns of 2D array
# [[6,-8,73,-110],[np.nan,-8,0,94]]
#------------------------------------------------------------------------------------------------------------
import numpy as np
array = np.array([[6, -8, 73], [-110, np.nan, -8], [0, 94, 5]])
array[np.isnan(array)] = 0
array[[0, 2]] = array[[2, 0]]
array[:, [0, 2]] = array[:, [2, 0]]
print("Modified Array:\n", array)
print('\n')
#-----------------------------------------------------------------
#Question(2):- Move axes of 3D array to new positions
#-----------------------------------------------------------------
s=np.ones((2,3,4))
t=np.moveaxis(s,0,-1)
print('move axes of 3d\n',t.shape)
print('\n')
#-----------------------------------------------------------------
#Question(3):- Replace NaN values with average of columns
#-----------------------------------------------------------------
arr = np.array([[np.nan, 2, np.nan], [6, np.nan, 1], [7, 5, 9]])
col_means = np.nanmean(arr, axis=0)
inds = np.where(np.isnan(arr))
arr[inds] = np.take(col_means, inds[1])
print(arr)
print('\n')
#-----------------------------------------------------------------
#Question(4):-  Replace negative values with 0
#-----------------------------------------------------------------
arr = np.array([[3, -1, 2], [-7, 4, -2]])
arr[arr < 0] = 0
print(arr)
#-----------------------------------------------------------------
#Question(5):-  Study the Program (from Question 6):
# #Question(6):-6. Import NumPy as np
# arr1 = np.array([3, 4])
# arr2 = np.array([1, 0])
#-----------------------------------------------------------------
import numpy as np

arr1 = np.array([3, 4])
arr2 = np.array([1, 0])
avg = (arr1 + arr2) / 2
print("Average of NumPy arrays:", avg)
#-----------------------------------------------------------------
#Question(7):- Mean, Median, Mode of a 2D Array
#-----------------------------------------------------------------
import numpy as np
from scipy import stats
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[7, 8, 9],
                 [10, 11, 12]])
combined = np.concatenate((arr1, arr2), axis=0)

mean_val = np.mean(combined)
average_val = np.average(combined)
median_val = np.median(combined)
mode_result = stats.mode(combined, axis=None, keepdims=True)

# Output
print("Combined Array:\n", combined)
print("Mean:", mean_val)
print("Average:", average_val)
print("Median:", median_val)
print("Mode:", mode_result.mode[0])
#-----------------------------------------------------------------
#Question(8):-  Solve Linear Equations using linalg
# x - 2y + 3z = 9
# -x + 3y - z = -6
# 2x - 5y + 5z = 17
#-----------------------------------------------------------------
A = np.array([[1, -2, 3], [-1, 3, -1], [2, -5, 5]])
B = np.array([9, -6, 17])
solution = np.linalg.solve(A, B)
print("Solution of equations:", solution)
#---------------------------------------------------------------------------------------------------------------
#Question(9):-using customization matplotlib visualization , plot graph to compare your at least 2 sem result
#---------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
semesters = ['Sem 1', 'Sem 2']
marks = [7.8, 7.0]

plt.figure(figsize=(8, 6))
bars = plt.bar(semesters, marks, color='skyblue', edgecolor='black', width=0.5)
plt.title("Semester-wise Result Comparison", fontsize=16, fontweight='bold')
plt.xlabel("Semesters", fontsize=12)
plt.ylabel("Marks (out of 10)", fontsize=12)
plt.ylim(0, 10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, f"{height}", ha='center', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()


