#Assignment (2)
#----------------------------------------------------------------------------------------------------------
#Question 1:-
# In your last program where you find the total and
# percentage of a student's marks of 5 subject, find the grade of the student using conditional statement.
# Eg. grade 'A' if percentage is greator than or equals to 60, 'B' for  percentage is greator than or
# equals to 50 and less than 60,  'C' for  percentage is greator than or equals to 40 and less than 50,
# 'D' for  percentage is greator than or equals to 33 and less than 40, otherwise 'Fail'
#-------------------------------------------------------------------------------------------------------------
name = input("Enter student's name: ")
student_class = input("Enter class: ")
print("Enter marks out of 100 for 5 subjects:")
mark1 = float(input("Subject 1: "))
mark2 = float(input("Subject 2: "))
mark3 = float(input("Subject 3: "))
mark4 = float(input("Subject 4: "))
mark5 = float(input("Subject 5: "))
total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = (total / 500) * 100
if percentage >= 80:
    grade = 'A'
elif percentage >=60:
    grade = 'B'
elif percentage >=50:
    grade = 'C'
elif percentage >= 33:
    grade = 'D'
else:
    grade = 'Fail'
print("\n--- Student Report ---")
print("Name  :", name)
print("Class :", student_class)
print("Total Marks :", total)
print("Percentage :", round(percentage, 2), "%")
print("Grade :", grade)
print("\n")
# Question (2)
#---------------------------------------------------------------
# Input a number from user and find its factorial using for loop
#---------------------------------------------------------------
items = []
prices = []
while True:
    print("\n billing menu\n")
    print("1. Create Bill (Add Item)")
    print("2. Display Items and Prices")
    print("3. Display Total Amount")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter item name: ")
        price = float(input("Enter price of the item: "))
        items.append(item)
        prices.append(price)
        print(f"'{item}' added to bill.")

    elif choice == '2':
        if not items:
            print("No items in bill.")
        else:
            print("\nBill Details")
            for i in range(len(items)):
                print(f"{items[i]} - rs{prices[i]}")
            print("Total Amount: rs", sum(prices))

    elif choice == '3':
        print("Total Amount to Pay: rs", sum(prices))

    elif choice == '4':
        print("Thank you for using the billing system!")
        break

    else:
        print("Invalid choice! Please enter between 1 and 4.")
print("\n")
#--------------------------------------------------------------------------
#Question (3)
# Create a billing program using list. Program should have options to
# 1. Create Bill
# 2. Display Item Price and total bill amount
# 3. Display Total
# 4. Exit
# ------------------------------------------------------------------------
num = int(input("Enter a number: "))
factorial =1
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("Factorial of", num, "is", factorial)
print("\n")
#------------------------------------------------------------------------
# Question (4)
# 4(a)Program to find the smallest number in a list
numbers = [26, 16, 21, 30, 3, 1]
smallest = min(numbers)
print("Smallest number is:", smallest)
#4(b)Program to find the second greatest number in a list
numbers = [26, 16, 21, 30, 3, 1]
numbers.sort()
second_greatest = numbers[-2]
print("Second greatest number is:", second_greatest)
# 4(c)Program to find the second smallest number in a list
numbers = [26, 16, 21, 30, 3, 1]
numbers.sort()
second_smallest = numbers[1]
print("Second smallest number is:", second_smallest)
print("\n")




