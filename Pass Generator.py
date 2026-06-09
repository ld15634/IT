import random

def generate_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(letters) for i in range(length))

print("Welcome to the Random Password Generator.")

print("Would you like to generate a random password using a random string? (yes/no)")
answer = input()

if answer.lower() == "yes":

    while True:
        try:
            print("How long would you like your password to be?")
            length = int(input())

            if length > 0:
                break
            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print("Generating a random password using a random string...")

    random_string = generate_random_string(length)
    print(random_string)
    print("Here is your generated password.")

elif answer.lower() == "no":
    print("Thank you for using the Random Password Generator. Goodbye!")

else:
    print("Invalid input. Please enter 'yes' or 'no'.")

print("Would you like to generate another random password? (yes/no)")
answer = input()

if answer.lower() == "yes":

    while True:
        try:
            print("How long would you like your password to be?")
            length = int(input())

            if length > 0:
                break
            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    random_string = generate_random_string(length)
    print(random_string)
    print("Here is your generated password.")

elif answer.lower() == "no":
    print("Thank you for using the Random Password Generator. Goodbye!")

else:
    print("Invalid input. Please enter 'yes' or 'no'.")