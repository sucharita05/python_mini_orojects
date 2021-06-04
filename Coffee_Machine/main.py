from data import MENU, resources
import os

clear = lambda: os.system('cls')

    
def process_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many ten rupess?: ")) * 10
    total += int(input("how many five rupess?: ")) * 5
    total += int(input("how many two rupess?: ")) * 2
    total += int(input("how many one rupess?: ")) * 1
    return total


def cost_calculation(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    global money
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ₹{change} in change.")
        money += drink_cost
        return True
        
    
def make_coffee(drink_name, order_ingredients, drink_cost):

    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
        elif order_ingredients[item] < resources[item]:
            payment = process_coin()
            if cost_calculation(payment, drink_cost) == True:
                print(f"Here is your {drink_name} ☕️. Enjoy!")
                """Deduct the required ingredients from the resources."""
                for item in order_ingredients:
                    resources[item] -= order_ingredients[item]
            return True


money = 0
is_on = True

while is_on:
    user_input = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    

    if user_input == 'off':
        is_on = False
        clear()
    elif user_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ₹ {money}")
    else:
        # for key, value in MENU.items():
        #     if user_input == key:
        #         choice = key
        drink = MENU[user_input]
        drink_cost = drink['cost'] 
        make_coffee(user_input, drink['ingredients'], drink_cost)
             
                




