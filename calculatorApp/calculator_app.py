def add(a, b):
    answer = a + b
    print(f'{a} + {b} = {answer} \n')


def sub(a, b):
    answer = a - b
    print(f'{a} - {b} = {answer} \n')


def mult(a, b):
    answer = a * b
    print(f'{a} * {b} = {answer} \n')


def div(a, b):
    answer = a / b
    print(f'{a} / {b} = {answer} \n')


while True:
    print("Welcome to the calculator app. \n Please select an operation: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit")

    select = input("Select an operation: ")

    if select == '1' or select == '1.':  # Addition
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        add(a, b)
    elif select == '2' or select == '2.':  # Subtraction
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        sub(a, b)
    elif select == '3' or select == '3.':  # Multiplication
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        mult(a, b)
    elif select == '4' or select == '4.':  # Division
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        div(a, b)
    elif select == '5' or select == '5.':
        print("Exiting the calculator app")
        exit()
