import sys
from create_account import username_availability

# greeting to app
print("Hello there!\nHow would you like to proceed?")

# list of choices
choices = ['1', '2']

# loop until right input
while True:

    # providing choices
    print("\n[1] Log In\n[2] Create account\n[3] Quit")

    # getting input
    user_input = input('\nYour choice: ')

    # if right input
    if user_input in choices:
        user_input = int(user_input)
        break

    # if user wants to quit app
    if user_input == '3':
        print("\nAre you sure you want to quit?\n[1] Continue\n[2] Cancel")
        quit = input("\nYour choice: ")

        # if chosen to quit
        if quit == '1':
            sys.exit("Goodbye!") # stops python program
    
    if quit is None:
        # informing user
        print("Invalid response. Please try again!")

# next move depending on input
if user_input == 1:
    username = 'function from create_account.py'
elif user_input == 2:
    # start creating new account
    print("\nYou have chosen to create a new account.")

    # looping until confirmation of username selection
    while True:

        # asking user for chosen username
        username = input("Chose your username: ")

        # asking for confirmation
        confirm = input("\nIs {0} the correct username?\n[1] Continue\n[2] Try again".format(username))

        if confirm == '2':
            print("Chose again.\n")
            continue

        # check username availability
        check: bool = username_availability(username)

        # determining if available
        if check == False:
            print("\nUnfortunately the chosen username is already taken.\nPlease chose another one.\n")
        elif check == True:
            print("\nLucky you! The username you chose is available!\n")
            break
        else:
            sys.exit("\nSomething happened bruh WHAT THE FUCK")
    
    while True:
        # asking user of input
        password = input("\nNow it's time to chose your password: ")

        # asking for confirmation
        confirm = input("\nIs < {0} > the correct password?\n[1] Looks good\n[2] Do over".format(password))

        if confirm == '1':
            print("\nCoolio.\n")
            break

        if confirm == '2':
            print("\nChose again.\n")
            continue

print(f"\nYour username is {username}.")
print(f"Welcome to your EGO account.")
