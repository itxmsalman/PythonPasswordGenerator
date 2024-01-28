import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'b', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Kindly enter a positive figure")
            return value
        except ValueError:
            print("Invalid input. Kindly enter a positive figure")

print("Welcome to the Python Password Generator!")

nr_letters = get_valid_input("The amount of characters do you want in your password?\n")
nr_symbols = get_valid_input(f"Would you like a certain number of symbols?\n")
nr_numbers = get_valid_input(f"What is your preferred number of digits?\n")

# The remaining code is still the same.


def ordinary_pass():

    password = ""

    for characters in range(1, nr_letters + 1):
        password += random.choice(letters)

    for charaters in range(1, nr_symbols + 1):
        password += random.choice(symbols)

    for characters in range(1, nr_numbers + 1):
        password += random.choice(numbers)

    print(f" First Ordinary Password is {password}") 

def mixed_pass():

    password_list = []

    for characters in range(1, nr_letters + 1):
        password_list += random.choice(letters)

    for charaters in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    for characters in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)


    random.shuffle(password_list)
    
    mixed_pass = ""

    for characters in password_list:
        mixed_pass += characters

    print(f" Your Second Mixed Password is {mixed_pass}")

while True:
    
    print("\n Types Of Password:")
    print("1. Ordinary Password ")
    print("2. Mixed Password")

    selection = input("\nPlease enter the number of the action you want to perform: ")

    if selection == '1':
        ordinary_pass()
    elif selection == '2':
        mixed_pass ()
        break
    else:
        print("Please be sure the number you entered is valid.")