MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

# propmpt the user
# propmpt should also show every time the action has completed
# turn off the machine by entering the "off" it is for the maintainers

is_on = True
while is_on:
    user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_prompt != "espresso" and user_prompt != "latte" and user_prompt != "cappuccino":
        print("please select from the above options.")
    if user_prompt == "off":
        is_on = False
    elif user_prompt == "report":
        print(f"water: {resources["water"]}ml")
        print(f"milk:")
        print(f"coffee:")
        print(f"money:")

# print the report
