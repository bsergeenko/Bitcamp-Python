def main():
    greeting = input("greet me: ")
    print(value(greeting))


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif "h" in greeting[0]: 
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()