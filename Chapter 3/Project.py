#Define method which takes number and returns depending if even or odd a return value
def collatz(number):
    calculatedNumber = 0

    if number%2 == 0:
        calculatedNumber = number//2
    else:
        calculatedNumber = number * 3 + 1

    print(calculatedNumber)    
    return calculatedNumber

#User input

try:
    print("Input as number:")
    
    userInput = int(input())

    while userInput!= 1:
        userInput = collatz(userInput)

except ValueError:
    print("Please type in a number")
