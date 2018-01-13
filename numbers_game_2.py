from time import sleep

print("Choose a number from 0 to 1000 range. I will guess it in max 10 tries.")
sleep(2)
print("Thinking...")
sleep(2)

min_value = 0
max_value = 1000
rules = """
Enter:
    1 if I guesses too much
    2 if I guessed not enough
    3 if I guessed your number
What do you choose? """

try_num = 0

while try_num in range(0, 10):

    try:
        guess = (int(max_value - min_value) / 2) + min_value
        guess_msg = """
        I guess: {}""".format(int(guess))

        print(guess_msg)

        answer = int(input(rules))

        if answer == 1:
            max_value = guess
            try_num = try_num + 1
        elif answer == 2:
            min_value = guess
            try_num = try_num + 1
        elif answer == 3:
            print("Great! I won!")
            break
        else:
            print("Don't cheat!")
            try_num = try_num

    except Exception:
        print("Ups, something went wrong. Remember to enter 1, 2 or 3.")

if try_num == 10:
    print("End of trials. I didn't succeed :(")

