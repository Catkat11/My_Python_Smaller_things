from menu import MENU
from menu import resources
import menu
menu_continue = True


def asking():
    return input("What would you like? (espresso/latte/cappuccino): ")


def checking(choice):
    water = MENU[choice]["ingredients"]["water"]
    milk = MENU[choice]["ingredients"]["milk"]
    coffee = MENU[choice]["ingredients"]["coffee"]
    water_remaining = resources["water"]
    milk_remaining = resources["milk"]
    coffee_remaining = resources["coffee"]

    if water <= water_remaining and milk <= milk_remaining and coffee <= coffee_remaining:
        return True
    else:
        if water > water_remaining:
            print("Sorry there is not enough water")
        elif milk > milk_remaining:
            print("Sorry there is not enough milk")
        elif coffee > coffee_remaining:
            print("Sorry there is not enough coffee")
        return False


def payment(choice, profit=None):
    price = MENU[choice]["cost"]
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    paid = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    if paid >= price:
        rest = paid-price
        rest_round = round(rest, 2)
        print(f"Here is ${rest_round} in change.")
        menu.profit += price
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def making_coffee(choice):
    water = MENU[choice]["ingredients"]["water"]
    milk = MENU[choice]["ingredients"]["milk"]
    coffee = MENU[choice]["ingredients"]["coffee"]
    water_remaining = resources["water"]
    milk_remaining = resources["milk"]
    coffee_remaining = resources["coffee"]
    resources["water"] = water_remaining - water
    resources["milk"] = milk_remaining - milk
    resources["coffee"] = coffee_remaining - coffee

    print(f"Here is your {choice}. Enjoy!")


while menu_continue:
    choice = asking()
    if choice == "off":
        menu_continue = False
        break
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Profit: {menu.profit}")
    else:
        checked = checking(choice)
        if checked:
            check_payment = payment(choice)
            if check_payment:
                making_coffee(choice)
