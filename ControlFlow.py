# Date: 2.3.2020
# Greeting Function

# Declare Global Variables here...

name = input("What is your name: ")
x = 15

# Create Functions Here...
def greeting():
    print("Hello there " + name + ".")
    print(x)

def printSomething():
    x = 3
    print(x)

# Call Functions Here...

greeting()
printSomething()
print(x)