

#this is where my functions will go
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("this cannot be blank.")
        else:
            return response



#this is where the main routine will go

Ingredient = not_blank("What is the name of the ingredient? ")