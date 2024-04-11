def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response

#here is test
thing = not_blank("do you like oranges?")

if thing == "yes":
    print("yay!")

else:
    print("sad")