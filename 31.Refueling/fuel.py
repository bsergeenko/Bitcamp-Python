def main():
    fuel = input("Fraction: ")
    print (gauge(convert(fuel)))


def convert(fraction):
    x, y =fraction.split("/")

    x = int(x)
    y = int(y)
    if not x or y is int:
        raise ValueError ("Only integers are allowed")
    elif y == 0:
        raise ZeroDivisionError ("Error: Cannot divide by zero")
    elif x > y:
        raise ValueError ("percentage more than 100")
    else:
        fraction = round(x/y*100)
    return fraction


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()