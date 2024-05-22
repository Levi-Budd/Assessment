# this function makes sure that if the input isnt a number
# the program does not crash,
# and that it is more than 0

def num_check(question):

    while True:
        try:
            response = float(input(question))
            if response <= 0:
                print("please enter a value above 0")
            else:
                break

        except ValueError:
            print("please only enter a number.")
    return response


# here the is test, it will call the function and print the output.

grams = num_check("please enter a value")
print(grams)
