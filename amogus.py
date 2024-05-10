import re

response = input("what is your name ")

while not re.match("[a-zA-Z]", response):
    print("Please only enter letters")
    response = input("what is your name ")

print(f"Thank you Mr. {response}") 