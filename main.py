"""Main file to run the coffee machine program"""
from os import system
from coffee import MENU, resources

PROFIT = 0

def report():
    """Print the coffee machine resources"""
    print(f"Water: {resources['water']}ml\n"
          f"Milk:  {resources['milk']}ml\n"
          f"Beans: {resources['coffee']}g\n"
          f"Money: ${PROFIT}")
    input()
    system("clear")
    return resources

def display_coffees():
    """Prints out the coffees and price"""
    print("COFFEE BAR:")
    for drink, option in MENU.items():
        print(f"{drink.title()}: ${option['cost']}")

def enough_resources(order_ingredients):
    """Checks to see if the machine has enough resources for the order"""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def insert_payment():
    """Returns the total of all the coins"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * .25
    total += int(input("how many dimes?: ")) * .10
    total += int(input("how many nickles?: ")) * .05
    total += int(input("how many pennies?: ")) * .01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        global PROFIT
        PROFIT += drink_cost
        cust_change = round(money_received - drink_cost, 2)
        print(f"\nDispensing your change: ${cust_change}")
        return True
    else:
        print("Not enough, refunding payment.")
        return False

def make_coffee(drink_name, order_ingredients):
    """deduct the machine's ingredients based on the order"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

MACHINE_ON = True
while MACHINE_ON:
    display_coffees()
    request = input("\nWhat would you like to order? Or type 'off'\n")
    if request == "off":
        MACHINE_ON = False
    elif request == "report":
        report()
    else:
        drink = MENU[request]
        if enough_resources(drink["ingredients"]):
            payment = insert_payment()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(request, drink["ingredients"])
                input()
                system("clear")
