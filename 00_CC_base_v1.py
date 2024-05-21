

#this is where my functions will go


#this function checks if the response is not blank and returns input
def not_blank(question):
    while True:
        response = input(question)
        
        if response == "":
            print("this cannot be blank. ")
        else:
            return response


#this function only accepts floats and returns input
def num_check(question):

    while True:
        try:
            response = float(input(question))
            if response <= 0:
                print("please enter a value above 0 ")
            else:
                break

        except ValueError:
            print("please only enter a number. ")
    return response

#this function calculates the cost of the amount of ingredients and appends to "list"
def calculate(list):
    amt_per = list[3] / list[1]
    cost_per = list[2] / amt_per
    rounded = round(cost_per, 2)

    global total
    total += rounded

    global items
    items.append(list[0]) 
    
    
    print(f"it will cost ${rounded} of {list[0]}")

#this function makes sure an input is only yes or no, and returns yes/no.
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes/no")

#this is where the main routine will go

total = 0
items = []

name = not_blank("What is the name of your recipe? ")
#test

servings = num_check("How many servings are there? ")

#this loop gets all the values to calculate the cost
#then asks if the user has finished inputing ingredients.
while True:

    ingredient = not_blank("What is the name of the ingredient? ")

    amount = num_check("how many grams of this is needed? ")

    pkt_price = num_check("how much does a bought packet of this ingredient cost? ")

    packet = num_check("How many grams is inside a bought packet of this ingredient? ")

    list = [ingredient, amount, pkt_price, packet]

    cost = calculate(list)

    per_serve = round(total / servings, 2)


    #code that checks if the user is finished or not.
    finished = yes_no("are you finshed? yes/no ")
    if finished == "yes":
        unpacked = ", ".join(items)
        print(f"the ingredients are {unpacked} which comes to a total of ${total}, it will cost ${per_serve} to make {servings} servings of {name}")
        break
    elif finished == "no":
        continue



