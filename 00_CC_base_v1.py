

#this is where my functions will go


#this function checks if the response is not blank
def not_blank(question):
    while True:
        response = input(question)
        
        if response == "":
            print("this cannot be blank. ")
        else:
            return response


#this function only accepts floats.
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

#this function calculates the cost of the amount of ingredients
def calculate(list):
    amt_per = list[3] / list[1]
    cost_per = list[2] / amt_per
    rounded = round(cost_per, 2)

    global total
    total += rounded

    global items
    items.append(list[0]) 
    
    
    print(f"it will cost ${rounded} of {list[0]}")

#this is where the main routine will go

total = 0
items = []

name = not_blank("What is the name of your recipe?")

servings = num_check("How many servings are there? ")

while True:

    ingredient = not_blank("What is the name of the ingredient? ")

    amount = num_check("how many grams of this is needed? ")

    pkt_price = num_check("how much does a bought packet of this ingredient cost? ")

    packet = num_check("How many grams is inside a bought packet of this ingredient? ")

    list = [ingredient, amount, pkt_price, packet]

    cost = calculate(list)

    per_serve = round(total / servings, 2)



    a = input("are you finshed? yes/no ")
    if a == "yes":
        unpacked = ", ".join(items)
        print(f"the ingredients are {unpacked} which comes to a total of ${total}, it will cost ${per_serve} to make {servings} servings of {name}")
        break




