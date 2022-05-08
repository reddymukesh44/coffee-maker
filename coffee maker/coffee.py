
water = 100
milk = 50
coffee = 100
money = 0 

def rep():
    global water
    global milk
    global coffee
    global money
    print(f"Water = {water}ml")
    print(f"milk = {milk}ml")
    print(f"coffee = {coffee}ml")
    print(f"money = {money}ml")

def collectmoney():
    quaters = input("how many quarters?:")
    dimes = input("how many dimes?:")
    nickles = input("how many nickles?:")
    pennies = input("how many pennies?:")
    return (quaters * 0.25) + (dimes *  0.10) + (nickles * 0.05) + (pennies * 0.01)

def resourcecheck(resou):    
    global water
    global milk
    global coffee
    global money
    
    if resou == "espresso":
        if water >= 50 and coffee >= 12:
            return True

tempmoney = 0
while True:
    menu = input("What would you like? (espresso/latte/cappuccino): ")
    if menu.lower() == "report":
        rep()
    elif menu == "espresso":
        tempmoney == collectmoney()
        mon = True
        while mon == True
            if tempmoney < 1.5:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money = money + 1.5
                print(f"Here is ${tempmoney - 1.5} in change.")
                mon = False
                tempmoney = 0
        if resourcecheck("espresso") == True:
            continue
        else
