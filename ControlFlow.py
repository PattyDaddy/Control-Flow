
## Date: 2.3.2020
## Programmer: Patricio Ortiz

## Declare Global Variables here...

# name = input("What is your name: ")
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

## Call Functions Here...

# greeting()
# printSomething()
# print(x)
printNumber(15)
printNumber(16)