# this function makes sure that the program doesnt crash
# if the user inputs nothing.

def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response

# here the is test, it will call the function and print the output.


answer = not_blank("do you like oranges?")
print(answer)
