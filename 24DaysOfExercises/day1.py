"""Question #1

Instructions: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.     

Hints: Consider use range(#begin, #end) method.
"""
# solved using for loop
range1 = range(2000, 3201)
for i in range1:
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=",")

# solved using generators and list comprehension
print(*(i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0), sep=",")

"""Question #2

Instructions: Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320     

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""
# solved using for loop
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print('Factorial does not exist for negative numbers')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}")

# solved using while loop
num2 = int(input("Enter a number: "))
factorial2 = 1
i = 1
while i <= num2:
    factorial2 = factorial2 * i
    i += 1
print(f"The factorial of {num2} is {factorial2}")

"""Question #3

Instructions: With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary.Suppose the following input is supplied to the program: 8  

Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.Consider use dict()
"""
# solved using for loop
usrNum = int(input("Enter a number: "))
dict1 = {}
for i in range(1, usrNum + 1):
    dict1[i] = i * i
print(dict1)

# solved using dictionary comprehension
usrNum2 = int(input("Enter a number: "))
dict2 = {i: i * i for i in range(1, usrNum2 + 1)}
