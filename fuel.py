while True:
    try:
        fuel = input("Fraction: ")
        x, y =fuel.split("/")

        x = int(x)
        y = int(y)
        percentage = round(x/y*100)

        if percentage <= 1:
            print("Tank is essentially empty")
        elif percentage >= 99:
            print("Tank is essentially full")
        else:
            print(f"{percentage}%")

    except ValueError:
       print("You need whrite the number")
    except ZeroDivisionError:
        print ("Error: Cannot divide by zero")
    else:
        break


