# Assignment(3)
# question 1:- basic maths operations
#-----------------------------------------
def basic_math_operations(a,b):
    print("Addition:", a+b)
    print("Subtraction:", a-b)
    print("Multiplication:", a*b)
    if b != 0:
        print("Division:", a/b)
    else:
        print("Division: Cannot divide by zero")
# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("\n--- Math Operation Results ---")
basic_math_operations(num1, num2)
print("\n")

#-----------------------------------3
#question 2:- Palindrome Number Check
# ----------------------------
# Function to check palindrome
def is_palindrome(number):
    original = str(number)
    reversed_num = original[::-1]
    return original == reversed_num
# Input from user
num = int(input("\nEnter a number to check Palindrome: "))
# Check and print result
if is_palindrome(num):
    print(f"{num} is a Palindrome Number.")
else:
    print(f"{num} is NOT a Palindrome Number.")
print("\n")


