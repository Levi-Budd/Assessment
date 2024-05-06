

#this is where my functions will go


#this function checks if the response is not blank
def not_blank(question):
    while True:
        response = input(question)
        
        if response == "":
            print("this cannot be blank.")
        else:
            return response


#this function only accepts floats.
def num_check(question):

    while True:
        try:
            response = int(input(question))
            if response <= 0:
                print("please enter a value above 0")
            else:
                break

        except ValueError:
            print("please only enter a number.")
    return response


#this is where the main routine will go

servings = num_check("How many servings are there?")

while finished == False:
    ingredient = not_blank("What is the name of the ingredient? ")
    
    amount = num_check("how many grams of this is needed?")

    pkt_price = num_check("how much does a bought packet of this ingredient cost?")
    
    packet = not_blank("How many grams is inside a bought packet of this ingredient?")




