import random

print ("Welcome to the Random Password Generator.")

print ("Would you like to generate a random password using a random string? (yes/no)")
answer = input()
if answer.lower() == "yes":
    print ("How long would you like your password to be?")
    length = int(input())
    print ("Generating a random password using a random string...")
    #print(random_string)

else answer.lower() == "no":
    print ("Thank you for using the Random Password Generator. Goodbye!")
else:    print ("Invalid input. Please enter 'yes' or 'no'.")




def generate_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(letters) for _ in range(length))
if __name__ == "__main__":
    random_string = generate_random_string(length)
print(random_string)
print("Here is your generated password.")

print ("Would you like to generate another random password? (yes/no)")
answer = input()
if answer.lower() == "yes":
    print ("How long would you like your password to be?")
    length = int(input())

elif answer.lower() == "no":
    print ("Thank you for using the Random Password Generator. Goodbye!")
else:    print ("Invalid input. Please enter 'yes' or 'no'.")