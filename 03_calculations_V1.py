# this function calculates the cost of the amount of ingredients
# and appends to "list"
# it also outputs the cost and the item name
# to make sure the user can check to see if its wrong


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
# my test routine will first get the variables
# then add them together in a list.
# it will then run the calculate function and output the results if
# the user is finished.


total = 0
items = []

while True:
    ingredient = input("What is the name of the ingredient? ")

    amount = float(input("how many grams of this is needed? "))

    pkt_price = float(input("how much does a bought packet of this\
                             ingredient cost? "))

    packet = float(input("How many grams is inside a bought packet of this\
                          ingredient? "))

    list = [ingredient, amount, pkt_price, packet]

    cost = calculate(list)

    a = input("are you finshed? yes/no ")
    if a == "yes":
        unpacked = ", ".join(items)
        print(f"the ingredients are {unpacked} which comes to a total\
               of ${total}")
