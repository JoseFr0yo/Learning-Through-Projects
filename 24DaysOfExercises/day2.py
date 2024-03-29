"""Question #4

Instructions: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

Suppose the following input is supplied to the program: 34,67,55,33,12,98     

Then, the output should be: ['34', '67', '55', '33', '12', '98']
                            ('34', '67', '55', '33', '12', '98')

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.tuple() method can convert list to tuple
"""

lis = input("Enter a sequence of comma-separated numbers: ").split(",")
tup = tuple(lis)
print(lis)
print(tup)


"""Question #5

Instructions: Define a class which has at least two methods:

    - getString: to get a string from console input
    - printString: to print the string in upper case.

Also please include simple test function to test the class methods.

Hints: Use init method to construct some parameters
"""


"""Question #6

Instructions: Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the 
following comma separated input sequence is given to the program: 100,150,180

The output of the program should be: 18,22,24

Hints: If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26).
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
