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

print ("\nCongrats homie, you's is right!!\n")


"""
Programmer: PattyDaddy
Date: 12.19.19
Program: 1 Through 10
"""

x = 1

# While loop will see if a condition has been met
# If not it will run again until the condition
# has been met

while x <= 10:
    print(x)
    x += 1