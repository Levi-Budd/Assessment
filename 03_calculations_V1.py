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
    pkt_needed = list[3] / list[1]
    per_pack = pkt_needed / list[2]
    rounded = round(per_pack, 2)

    global items
    items = 0
    items += rounded
    
    
    print(f"it will cost ${rounded} of {list[0]}")
    
    




# here goes my test routine
while True:
    ingredient = not_blank("What is the name of the ingredient? ")

    amount = num_check("how many grams of this is needed? ")

    pkt_price = num_check("how much does a bought packet of this ingredient cost? ")

    packet = num_check("How many grams is inside a bought packet of this ingredient? ")

    list = [ingredient, amount, pkt_price, packet]

    cost = calculate(list)
    print(cost)

    a = input("blah blah")
    if a == "xxx":
        print(items)




