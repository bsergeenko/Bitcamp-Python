greeting = input("greet me: ").lower().strip()

if greeting.startswith("hello"):
    print("$0")
elif "h" in greeting[0]: 
    print("$20")
else:
    print("$100")