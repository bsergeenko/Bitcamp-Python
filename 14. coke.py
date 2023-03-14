amount = 0

while amount < 50:
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        amount += coin
        if amount < 50:
            print(f"Amount Due: {50-amount} ")
        else:
            print (f"Change Owed: {amount - 50} ")
    else:
        print(f"Amount Due: {50-amount} ")