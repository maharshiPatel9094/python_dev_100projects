import art

# write all the four functions
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

# adding this 4 values in  the dictionaries
operations = {
    "+" : add,
    "-": subtract,
    "*":multiply,
    "/":divide,
}

# use the dictionary opearations to perform the calculations
# print(operations["*"](4,8))


def calculator():
    print(art.logo)
    should_continue = True
    num1 = input("What is your first number?: ")

    while should_continue:
        for key in operations:
            print(key)
        opearation_symbol = input("Pick an operation: ")
        num2 = input("What is the next number?: ")
        answer = operations[opearation_symbol](num1,num2)
        print(f"{num1} {opearation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if choice == 'y':
            num1 = answer
            for key in operations:
                print(key)
            opearation_symbol = input("Pick an operation: ")
            num2 = input("What is the next number?: ")
            answer = operations[opearation_symbol](num1, num2)
            print(f"{num1} {opearation_symbol} {num2} = {answer}")
        else:
            should_continue = False
            print("\n" * 20)
            calculator()


calculator()