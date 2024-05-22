

def yes_no(question):
    # this function makes sure an input is only yes or no, and returns yes/no.
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes/no")