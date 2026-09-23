print("--- Welcome to Treasure Island ---")
choice1 = input('You are at a crossroad. Type "left" or "right": ').lower()

if choice1 == "left":
    choice2 = input('You came to a lake. Type "wait" for a boat or "swim" to swim across: ').lower()
    if choice2 == "wait":
        choice3 = input("Which door do you choose? Red, Yellow, or Blue: ").lower()
        if choice3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("Game Over! It's a trap.")
    else:
        print("Attacked by alligators. Game Over!")
else:
        print("Fell into a hole. Game Over!")