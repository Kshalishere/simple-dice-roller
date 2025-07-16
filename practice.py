import random

while True:
    x = input("Enter the number of sides for your dice, to quit, type quit: ")
    if x.lower() == "quit":
        break
    if not x.isdigit() or int(x) < 1:
        print("Please enter a positive integer.")
        continue
    dice = random.randint(1, int(x))
    print(f"Out of a {x}-sided dice, the dice landed on {dice}")

    
