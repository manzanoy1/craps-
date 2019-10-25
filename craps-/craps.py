#Yanira Manzano
#21/10/2019
#Project: Craps!

import random
import sys

print("""Hello player! Welcome to Craps!
Play Game or Quit?""")

option = input('> ')

if option == "play game":
    username = input("Please enter your name:")
    print(f"Welcome {username}, to craps!")
    print("Enter your coins that you will have.")
    coins = int(input('> '))

elif option == "quit":
    sys.exit()

while coins > 0 and bet > 0:
    print("Okay, how much do you want to bet on this round?")
    bet = int(input("> "))

    roll = random.randint(2, 12)
    print(f"You have rolled {roll}.")

    if roll == 7 or roll == 11:
        print(f"Hey {username}, you won! :D")
        coins = coins + bet
        print(f"{username} have now {coins} on his/her pocket.")

    elif roll == 2 or roll == 3 or roll == 12:
        print(f"Aw you lost this time, {username}. :(")
        coins = coins - bet
        print(f"{username} have now {coins} on his/her pocket.")

    else:
        print(f"You just encountered with {roll}. In this case you have to roll that value again to win, else you lose.")
        print(f"Don't lose hope, {username}!")
        encounter = roll

        if roll == encounter:
            coins = coins +  bet
            print(f"{username}! You won this bet with the roll of {roll}!")
            print(f"{username} have now {coins} on his/her pocket.")

        else:
            coins = coins - bet
            print(f"Damn {username}, you lost this bet with the roll of {roll}.")
            print(f"{username} have now {coins} on his/her pocket.")


print(f"Would you like to play again, {username}?")
choice = input('> ')
if choice == "yes":
    if bet > coins:
            print(f"{username}, you just bet more than you have in your pocket. So I have to end here. Goodbye {username}.")
elif choice == "no":
    print(f"Well see ya, {username}!")
    sys.exit()
else:
    bet = 0


