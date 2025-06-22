# Assignment(1)

# ***********************************************************************************
# Question 1:-
# Write a python program that takes in a student name, class.
#  It should also take in five subject marks of the students
#  and find the total mark and percentage. 
# Display a result in such a way that their name, class,  and percentage are printe
# ************************************************************************************

name = input("Enter student's name: ")
student_class = input("Enter class: ")
print("Enter marks of 5 subjects:")
mark1 = int(input("Subject 1: "))
mark2 = int(input("Subject 2: "))
mark3 = int(input("Subject 3: "))
mark4 = int(input("Subject 4: "))
mark5 = int(input("Subject 5: "))

# Calculating total marks and percentage of five subjects
total_marks = mark1+mark2+mark3+mark4+mark5
percentage = (total_marks/500)*100
# Displaying result of student
print("\n****** Student Report ******")
print("Name:",name)
print("Class:",student_class)
print("Total Marks:",total_marks)
print("Percentage:",round(percentage,2),"%")
print("\n********************")

# **************************************************************
# Question (2):-
# Input 2 strings concatinate them and store in another variable.
# then perform generally used string methods on it
# ***************************************************************
str1 = input("\nEnter first string: ")
str2 = input("Enter second string: ")
concatinate = str1 + str2
print("\nConcatenated String:", concatinate)

# String Methods
print("Upper Case:", concatinate.upper())
print("Lower Case:",concatinate .lower())
print("Title Case:", concatinate.title())
print("Length of String:", len(concatinate))
print("Does string contain 'a'?:",'a' in concatinate)
