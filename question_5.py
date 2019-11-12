#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on November 2019
# This program asks user to enter how many numbers
# they want to add. User enters numbers that are
# to be added, and positive even odd and negative answers
# are displayed


def main():
    loop_counter = 0
    even_answer = 0
    odd_answer = 0
    neg_answer = 0

    print("This will add and print out the sum of all positive even numbers,")
    print("the sum of all positive odd numbers and the sum of all negative")
    print("numbers")
    print("")

    # input
    user_ntry = input("Enter how many numbers you want to add: ")
    print("")

    # process
    try:
        user_loops = int(user_ntry)
        for loop_counter in range(user_loops):
            user_nput = input("Enter a number you want to add: ")
            try:
                int_check = int(user_nput)
                if int_check > 0:
                    if (int_check % 2 == 0):
                        even_answer = even_answer + int_check
                    else:
                        odd_answer = odd_answer + int_check
                else:
                    neg_answer = neg_answer + int_check
            except ValueError:
                print("Enter an integer. ")
        print("")
        print("The sum of the positive even numbers is: {}"
              .format(even_answer))
        print("The sum of the positive odd numbers is: {}".format(odd_answer))
        print("The summ of the negative numbers is: {}".format(neg_answer))
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
