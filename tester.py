
# here is my main routine, change prices at will.

burger = 4.00
fries = 2.00
drink = 3.00
hotdog = 4.00
total = 0.00
items = []
print('Welcome to fatty burger. our menu is burger 4.00, fries 2.00, hotdog 4.00 and drink 3.00 ')

while True:
    item1 = input('What would you like? type "finish" when you are done with your order. ') 

    if item1 == 'finish':
        #total = get_total(list)
        unpacked = ", ".join(items)
        print(f"Your order is {unpacked} which come to a total of {total} ")
        break

    elif item1 == 'fries':
        print(f'your item is a fries at ${fries} ')
        total += fries
        
        items.append("fries")

    elif item1 == 'hotdog':
        print(f'your item is a hotdog at ${hotdog} ')
        total += hotdog
        
        items.append("hotdog")


    elif item1 == 'drink':
        print(f'your item is a drink at ${drink} ')
        total += drink
        
        items.append("drink")

    if item1 == 'burger':
        print(f'your item is a burger at ${burger} ')
        total += burger
        
        items.append("burger")

    else:
        print('your options are burger $4.00, fries $2.00, hotdog $4.00 and drink $3.00.')
