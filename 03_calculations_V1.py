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
            response = int(input(question))
            if response <= 0:
                print("please enter a value above 0")
            else:
                break

        except ValueError:
            print("please only enter a number.")
    return response
   
def calculate(list):
    per_pack = list[3] // list[1]
    cost = list[2] / per_pack

    list = [per_pack, cost]
    return(list)




# here goes my test routine


ingredient = not_blank("What is the name of the ingredient? ")

amount = num_check("how many grams of this is needed?")

pkt_price = num_check("how much does a bought packet of this ingredient cost?")

packet = not_blank("How many grams is inside a bought packet of this ingredient?")

list = [ingredient, amount, pkt_price, packet]

cost = calculate(list)
print(cost)


