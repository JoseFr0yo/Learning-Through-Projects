# Generate a random password? Yes or no
# If no, exit program
# If yes, how many characters? 8-32
# If yes, include special characters? Yes or no
# If yes, include numbers? Yes or no
# If yes, include lowercase letters? Yes or no
# If yes, include uppercase letters? Yes or no
# If yes, generate password and display to user
print('Welcome to the Random Password Generator App \n')
prg_start = input("Would you like to generate a random password? (yes/no): ")
if prg_start.lower() == "no":
    print("Thank you for using the Random Password Generator App. Goodbye.")
    exit()
elif prg_start.lower() == "yes":
    pass_len = int(
        input("What is the minimum length of the password (8-32): "))
