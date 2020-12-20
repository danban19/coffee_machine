class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups_left = 9
        self.money = 550
        self.running = False

    def making_coffee(self):  # choosing a function of the coffee machine
        self.running = True
        self.action = input("Write action (buy, fill, take, remaining, exit):\n")
        if self.action == "buy":
            self.buy()
        if self.action == "fill":
            self.fill()
        if self.action == "take":
            self.take()
        if self.action == "remaining":
            self.remaining()
        if self.action == "exit":
            exit()

    def buy(self):  # choosing coffee to buy
        print("")
        self.chosen_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if self.chosen_coffee == "back":
            self.making_coffee()
        if self.chosen_coffee == "1":
            if self.water - 250 < 0:
                print("Sorry, not enough water!")
            elif self.beans - 16 < 0:
                print("Sorry, not enough coffee beans!")
            elif self.cups_left - 1 < 0:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups_left -= 1
        if self.chosen_coffee == "2":
            if self.water - 350 < 0:
                print("Sorry, not enough water!")
            elif self.milk - 75 < 0:
                print("Sorry, not enough milk!")
            elif self.beans - 20 < 0:
                print("Sorry, not enough coffee beans!")
            elif self.cups_left - 1 < 0:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups_left -= 1
        if self.chosen_coffee == "3":
            if self.water - 200 < 0:
                print("Sorry, not enough water!")
            elif self.milk - 100 < 0:
                print("Sorry, not enough milk!")
            elif self.beans - 12 < 0:
                print("Sorry, not enough coffee beans!")
            elif self.cups_left - 1 < 0:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups_left -= 1
        print('')
        self.making_coffee()

    def fill(self):  # choosing resources to fill
        print("")
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups_left += int(input("Write how many disposable cups of coffee do you want to add:"))
        print('')
        self.making_coffee()

    def take(self):  # taking money from the coffee machine
        print("")
        print("I gave you ${}".format(self.money))
        self.money = 0
        print('')
        self.making_coffee()

    def remaining(self):  # checking resources left
        print("")
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.cups_left))
        print("{} of money".format(self.money))
        print('')
        self.making_coffee()

    def exit():
        self.making_coffee()

machine = CoffeeMachine()
machine.making_coffee()