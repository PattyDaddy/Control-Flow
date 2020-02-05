
## Date: 2.3.2020
## Programmer: Patricio Ortiz

## Declare Global Variables here...

name = input("What is your name: ")
x = 15

## Create Functions Here...

## Greeting Function
def greeting():
    print("Hello there " + name + ".")
    print(x)

## Functions & Local Variable x
def printSomething():
    x = 3
    print(x)

# Functions & Parameters
def printNumber(age): ##function name = printNumber with a PARAMETER of age
    print(age)

# Default Parameter Values
def printTwoNumbers(x,y = 71):
    print("First Parameter(Number): " + str(x))
    print("Second Parameter(Number): " + str(y))

# Print Sum
def printSum(x,y): ## x and y are PARAMETERS
    print(x + y)

# Print Multiple Times
def printMultipleTimes(string, times): ## ILoveComputerScience has STRING a data type
    for i in range(times):
        print(string)


## Call Functions Here...

print("\n***Greetings Function***\n")
greeting()
print("\n***Print Something Function***\n")
printSomething()

print(x)

print("\n***Print Number Function***\n")
printNumber(15)
printNumber(16)

print("\n***Print Two Numbers Function***\n")
printTwoNumbers(23,78)

print("\n***Default Parameter Values Function***\n")
printTwoNumbers(45)

print("\n***Print Sum Function***\n")
printSum(1,17)

print("\n***Print Multiple Times Function***\n")
printMultipleTimes("ILoveComputerScience", 13)

print("\n***I hope you enjoyed my functions!!***\n")