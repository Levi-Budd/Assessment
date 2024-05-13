#this is me importing the random module
#the code WILL break if you touch this
import random

#this checks if an input is yes or no
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes/no")

#here is my num_check function, makes sure that the id is valid.
def num_check(question):
    #edit the max ID size as you want.
    max = 9999

    while True:
        try:
            response =  int(input(question))
            if response <= 0:
                print("Please enter a valid ID between 0001 and 9999")

            elif response > max:
                print("Please enter a vaild id between 0001 and 9999")

            else:
                break

        except ValueError:
            print("please only enter an ID.")
    return response

#down here is my main routine

list = []
tracker = 0

counter = num_check("how many ID's would you like to add to the raffle")
#counter = 4


while counter > tracker:
    id = num_check("Hello, please type your RSA number. ")
    if id in list:
        print("You cannot enter the same id twice.")
        continue
    else:
        answer = yes_no(f"You entered {id}, is this correct? (yes/no) ")
        while True:
            if answer == "yes":
                tracker += 1 #adds 1 to tracker so the loop doesnt keep repeating forever
                list.append(id)
                break
            else:
                break
            

winner = random.choice(list)

index = min(range(len(list)), key=lambda i: abs(list[i]-winner)) #this gets where the winner is in the list
del list[index] # this deletes the winner from the list

value = min(enumerate(list), key=lambda x: abs(x[1]-winner)) #this gets the closest to the winner in the list
closest = value[1] # this assigns the closest to a variable

print(f"The lucky winner is {winner}, and the closest is {closest}")


    