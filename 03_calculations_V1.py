# here are my functions
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response

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

def calculate(list):
    amt_per = list[3] / list[1]
    cost_per = list[2] / amt_per
    rounded = round(cost_per, 2)

    global total
    total += rounded

    global items
    items.append(list[0]) 
    
    
    print(f"it will cost ${rounded} of {list[0]}")


# here goes my test routine
total = 0
items = []

while True:
    ingredient = not_blank("What is the name of the ingredient? ")

    amount = num_check("how many grams of this is needed? ")

    pkt_price = num_check("how much does a bought packet of this ingredient cost? ")

    packet = num_check("How many grams is inside a bought packet of this ingredient? ")

    list = [ingredient, amount, pkt_price, packet]

    cost = calculate(list)
    

    a = input("are you finshed? yes/no")
    if a == "yes":
        unpacked = ", ".join(items)
        print(f"the ingredients are {unpacked} which comes to a total of ${total}")



