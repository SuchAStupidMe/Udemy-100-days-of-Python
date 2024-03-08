# Coffee Machine Project

def check_resources(recipe, resources):
    insufficient_resources = []
    for ingredient, required_amount in recipe.items():
        if ingredient in resources and resources[ingredient] < required_amount:
            insufficient_resources.append(ingredient)

    if insufficient_resources:
        return False, insufficient_resources
    else:
        return True, None


def process_coins(cost):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    value = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    if value < cost:
        return False, None
    change = round(value - cost, 2)
    if change == 0:
        return True, None
    return True, change


def make_coffee(recipe, resources):
    for ingredient, required_amount in recipe.items():
        if ingredient in resources:
            resources[ingredient] -= required_amount
    return resources


def complete_coffee(MENU, resources, money, prompt):
    result, insufficient = check_resources(MENU[prompt]['ingredients'], resources)
    if not result:
        print(f"Insufficient resources for {', '.join(insufficient)} in the recipe.")
        return resources, money

    result, change = process_coins(MENU[prompt]["cost"])
    if not result:
        print("Sorry that's not enough money. Money refunded.")
        return resources, money
    if change > 0:
        print(f"Here is ${change} dollars in change.”")

    resources = make_coffee(MENU[prompt]['ingredients'], resources)
    money += MENU[prompt]['cost']

    print(f"Here is your {prompt}. Enjoy!")
    return resources, money


def coffee_machine():
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
        "water": 1300,
        "milk": 1200,
        "coffee": 150,
    }

    money = 0.0

    while True:
        prompt = input("What would you like? (espresso/latte/cappuccino): ")
        match prompt:
            case "off":
                break

            case "report":
                report = '\n'.join([f'{k.capitalize()}: {v}' for k, v in resources.items()]) + f'\nMoney: {money}'
                print(report)

            case "espresso":
                resources, money = complete_coffee(MENU, resources,money, prompt)

            case "latte":
                resources, money = complete_coffee(MENU, resources, money, prompt)

            case "cappuccino":
                resources, money = complete_coffee(MENU, resources, money, prompt)


coffee_machine()
