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

# function for checking ingredients are sufficient or not
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made and false when ingredients are not sufficient"""
    for item in order_ingredients:
        # resources[itme] -> 300,200,100 gives the value
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from the coins inserted"""
    print("Please insert coins.")
    quarters = int(input("How many Quarters you have ?")) * 0.25
    dimes = int(input("How many dimes you have ?")) * 0.1
    nickles = int(input("How many nickles you have ?")) * 0.05
    pennies = int(input("How many pennies you have ?")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total

def is_transaction_successful(money_received,drink_cost):
    """Return True when payment is accepted and return false when money is not sufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} of change. ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False

is_on = True
while is_on:
    user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_prompt != "espresso" and user_prompt != "latte" and user_prompt != "cappuccino":
        print("please select from the above options.")


    if user_prompt == "off":
        is_on = False
    # print the report
    elif user_prompt == "report":
        print(f"water: {resources["water"]}ml")
        print(f"milk: {resources["milk"]}")
        print(f"coffee: {resources["coffee"]}")
        print(f"money: ${profit}")

# check the resoureces are sufficient or not
    else:
        drink = MENU[user_prompt]
        if is_resource_sufficient(drink["ingredients"]):
            # process coins
            payment = process_coins()
            is_transaction_successful(payment,drink["cost"])
