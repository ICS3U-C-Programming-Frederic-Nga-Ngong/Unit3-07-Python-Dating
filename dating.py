#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 18 2008
# Tell the user if he can date my grandchild or not.


def main():

    # Get the age of the user
    number_str = input("Enter your age: \n")

    # Verify if the age is an integer
    try:

        number_int = int(number_str)

        # Verify if the age is greater than 25 and less 40
        if number_int > 25 and number_int < 40:

            print("You can date my grandchild.")

        elif number_int < 0:
            print("Please, enter a valid number.")

        # if not the tell the user
        else:
            print("Sorry, you can not date my grandchild.")

    # If the age is not a valid number, the tell the user
    except ValueError:
        print("{} is not a valid number." .format(number_str)) 

    # And whatever the result, thank the user for using the code
    finally:
        print("Thanks for playing.")


if __name__ == "__main__":

    main()
