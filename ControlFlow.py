
# Programmer: PattyDaddy
# Date: 1.20.20
# Program: Double For Loop

for i in range(3):
    print("Outer For Loop " + str(i))
    for k in range(4):
        print ("\tInner for Loop " + str(k))



print("\n**********************\n")

"""
Programmer: Patricio Ortiz
Date: 1.23.20
Program: While Loop nested inside of a For Loop
"""

for i in range(4):
    print("For Loop: " + str(i))
    x = i
    while x >= 0:
        print("\tWhile Loop: " + str(x))
        x = x - 1
