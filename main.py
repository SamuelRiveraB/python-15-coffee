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
    "money": 2.5
}

on = True


def receive_coins(coffee):
    print("Please insert coins")
    qu = float(input("How many quarters? "))
    di = float(input("How many dimes? "))
    ni = float(input("How many nickles? "))
    pn = float(input("How many pennies? "))
    total = qu * 0.25 + di * 0.10 + ni * 0.05 + pn * 0.01
    print(f"That's ${total}")
    if total >= MENU[coffee]['cost']:
        print(f"Your change is {total - MENU[coffee]['cost']}")
        print(f"Enjoy your {coffee}")
        resources['water'] -= MENU[coffee]['ingredients']['water']
        if not coffee == 'espresso':
            resources['milk'] -= MENU[coffee]['ingredients']['milk']
        resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
        resources['money'] += MENU[coffee]['cost']
        return
    else:
        print("Not enough money")
        return


while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif choice == "off":
        on = False
    elif choice == "espresso":
        if resources['water'] >= MENU['espresso']['ingredients']['water']:
            if resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
                receive_coins("espresso")
            else:
                print("Sorry, there is not enough coffee")
        else:
            print("Sorry, there is not enough water")

    elif choice == "latte":
        if resources['water'] >= MENU['latte']['ingredients']['water']:
            if resources['milk'] >= MENU['latte']['ingredients']['milk']:
                if resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
                    receive_coins("latte")
                else:
                    print("Sorry, there is not enough coffee")
            else:
                print("Sorry, there is not enough milk")
        else:
            print("Sorry, there is not enough water")
    elif choice == "cappuccino":
        if resources['water'] >= MENU['cappuccino']['ingredients']['water']:
            if resources['milk'] >= MENU['cappuccino']['ingredients']['milk']:
                if resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
                    receive_coins("cappuccino")
                else:
                    print("Sorry, there is not enough coffee")
            else:
                print("Sorry, there is not enough milk")
        else:
            print("Sorry, there is not enough water")

