"""
Programmer: PattyDaddy
Date: 12.16.19
Program: Guess My Number
"""

myNumber = 7

print("\nGuess a number between One & Ten\n")

# Ask users to guess
guess = int(input("Enter a Guess: "))

# Keep asking users to guess my number until
# it is equal to myNumber
while guess != myNumber:
    print("\nNope, guess again: ")
    guess = int(input("Enter a Guess: "))

print ("\nCongrats homie, you's is right!!")