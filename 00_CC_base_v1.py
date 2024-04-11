

#this is where my functions will go
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Please input the name of the ingredient")
        else:
            return response



#this is where the main routine will go

cheese = not_blank("What is the name of the ingredient? ")
print("easy peasy.")