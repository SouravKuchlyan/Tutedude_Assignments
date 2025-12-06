# Task - 1 :- Check the number is odd or even.

num = int(input("Enter a Number :"))
print(num, "is an Even number") if num %2 == 0 else print (num, "is an Odd number")


# Task - 2 :-   Sum of Integers from 1 to 50 Using a Loop without using inbuilt sum.

total = 0

for i in range (1,51):
    total += i
print ("The Sum of the numbers from 1 to 50 is :- ", total)

# Sum of Integers from 1 to 50 Using a Loop with using inbuilt sum.

total = sum([i for i in range(1, 51)])
print("The Sum of the numbers from 1 to 50 is :- ", total)

    # Sum of Integers from 1 to 50 Using by for Loop.

total = sum(range(1,51))
print ("The Sum of the numbers from 1 to 50 is :- ", total)
