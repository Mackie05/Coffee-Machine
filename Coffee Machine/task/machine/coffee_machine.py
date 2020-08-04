import operator

# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")


water_supply = 400
milk_supply = 540
bean_supply = 120
cup_supply = 9
money_supply = 550


def supplies():
    print("The coffee machine currently has:")
    print(water_supply, "ml of water")
    print(milk_supply, "ml of milk")
    print(bean_supply, "grams of beans")
    print(cup_supply, "cups")
    print(money_supply, "of money")
    main_menu()


def purchase():
    global water_supply
    global milk_supply
    global bean_supply
    global cup_supply
    global money_supply

    user_option = input("Make a selection: 1 - Espresso, 2 - Latte, 3 - Cappuccino. back - main menu:")
    while cup_supply > 0:
        if user_option == 'back':
            main_menu()
        elif user_option == '1':
            if water_supply < 250:
                print("Sorry, not enough water.")
                main_menu()
            elif bean_supply < 16:
                print("Sorry, not enough beans.")
                main_menu()
            else:
                water_supply -= 250
                bean_supply -= 16
                money_supply += 4
                cup_supply -= 1
                print("I have enough resources, making you a coffee!")
        elif user_option == '2':
            if water_supply < 350:
                print("Sorry, not enough water.")
                main_menu()
            elif milk_supply < 75:
                print("Sorry, not enough milk.")
                main_menu()
            elif bean_supply < 20:
                print("Sorry, not enough beans.")
                main_menu()
            else:
                water_supply -= 350
                milk_supply -= 75
                bean_supply -= 20
                cup_supply -= 1
                money_supply += 7
                print("I have enough resources, making you a coffee!")
        elif user_option == '3':
            if water_supply < 200:
                print("Sorry, not enough water.")
                main_menu()
            elif milk_supply < 100:
                print("Sorry, not enough milk.")
                main_menu()
            elif bean_supply < 12:
                print("Sorry, not enough beans.")
                main_menu()
            else:
                water_supply -= 200
                milk_supply -= 100
                bean_supply -= 12
                cup_supply -= 1
                money_supply += 6
            print("I have enough resources, making you a coffee!")
        main_menu()


def restock():
    global water_supply
    global milk_supply
    global bean_supply
    global cup_supply
    water_supply += int(input("How much water would you like to add? (Measurements are in ml): "))
    milk_supply += int(input("How much milk? (Measurements are in ml): "))
    bean_supply += int(input("How much coffee bean (in grams)?: "))
    cup_supply += int(input("How many cups?: "))
    main_menu()


def cash_out():
    global money_supply
    print("$" + str(money_supply), "has been taken from the cash box.")
    money_supply -= money_supply
    main_menu()


def main_menu():
    user_action = input("Please select from the following: (buy, fill, take, remaining, exit):")
    if user_action == "buy":
        purchase()
    elif user_action == "fill":
        restock()
    elif user_action == "take":
        cash_out()
    elif user_action == 'remaining':
        supplies()
    elif user_action == 'exit':
        exit()


main_menu()


supplies()


# coffee_needed = int(input("Write how many cups of coffee you will need: "))
# print("For ", coffee_needed, " cups of coffee you will need:")
# print(coffee_water * coffee_needed, "ml of water")
# print(coffee_milk * coffee_needed, "ml of milk")
# print(coffee_beans * coffee_needed, "g of beans")

# cups_available = 0
# while water_supply >= coffee_water and milk_supply >= coffee_milk and bean_supply >= coffee_beans:
#     water_supply -= coffee_water
#     milk_supply -= coffee_milk
#     bean_supply -= coffee_beans
#     cups_available += 1
#
# if cups_available == coffee_needed:
#     print("Yes, I can make that amount of coffee")
# elif cups_available > coffee_needed:
#     print("Yes, I can make that amount of coffee (and even", cups_available - coffee_needed, "more than that)")
# else:
#     print("No, I can only make", cups_available, "cups of coffee")
