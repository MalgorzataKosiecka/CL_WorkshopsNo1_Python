from random import randint
from time import sleep

guessed = False
computer_number = randint(1, 100)

print("The computer draws a number from 1 to 100 range. Try to guess the number.")
sleep(2)

while not guessed:
    user_number_str = input("Guess the number: ")

    try:
        user_number_int = int(user_number_str)
    except ValueError:
        print("This is not a number.")
        continue

    if user_number_int == computer_number:
        print("You won!")
        guessed = True
    elif user_number_int < computer_number:
        print("Not enough!")
        continue
    else:
        print("Too much!")
        continue

