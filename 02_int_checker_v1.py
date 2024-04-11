#this function makes sure that an interger input does not crash,
#and that it is more than 0
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("please only enter a number.")
        
        else:
            if response <= 0:
                print("please enter a value above 0")


grams = num_check("What is the amount of the ingredient  in grams? ")
print(grams)
