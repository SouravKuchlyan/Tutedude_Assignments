# Task - 1

"""
ask 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
   o	Addition
   o	Subtraction
   o	Multiplication
   o	Division
"""
# Task - 1 Answers

# 1. Take user's first number and second number as input.
Num = float(input("Enter first number :"))
Num2 = float(input("Enter second number :"))

# 2. Making operations between two number & assining them in a variable.
A = Num + Num2
S = Num - Num2
D = Num / Num2
M = Num * Num2

# 3. Printing them each.
print ("Addition : ", A)
print ("subtraction : ", S)
print ("Divisition : ", D)
print ("Multiplication : ", M)



# Task - 2
"""
Create a Personalized Greeting.
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""

# Task - 2 Answer

# 1. Take user's first name and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# 2. Concatenate the first name and last name into a full name
full_name = first_name + " " + last_name

# 3. Print a personalized greeting message using the full name
print(f"Hello, {full_name}! Welcome to the python program.")