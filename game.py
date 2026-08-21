import random

def validate_input(text):
    num = -1
    while num < 1:
        try:
            num = int(input(text))
        except ValueError:
            continue
    return num

n = validate_input("Level: ")

item = random.randint(1, n)
guess = item + 1

while guess != item:
    guess = validate_input("Guess: ")
    if guess < item:
        print("Too small!")
    elif guess > item:
        print("Too large!") 
    else:
        print("Just right!")