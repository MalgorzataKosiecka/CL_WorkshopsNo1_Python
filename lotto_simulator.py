from random import sample

def lotto():

    user_list = input("Enter six numbers separated by commas: ").split(",")

    for number in user_list:

        if number.isdigit() and int(number) in range(1,50) and len(user_list) == 6 and \
                        len(user_list) == len(set(user_list)):
            user_list = [int(number) for number in user_list]
            user_list_sorted = sorted(user_list)
            computer_numbers = sorted(sample(range(1, 50), 6))
            guessed_numbers = set(user_list_sorted).intersection(computer_numbers)
            number_of_hits = len(guessed_numbers)

            if number_of_hits > 2:
                return ("""
                YOU WON!!! :)
                Your numbers: {}
                Numbers drawn by computer: {}
                You correctly hit: {}
                """.format(user_list_sorted, computer_numbers, number_of_hits))

            else:
                return ("""
                YOU DIDN'T WIN :(
                Your numbers: {}
                Numbers drawn by computer: {}
                You correctly hit: {}
                """.format(user_list_sorted, computer_numbers, number_of_hits))

        else:
            return ("You entered wrong numbers...")

print(lotto())

