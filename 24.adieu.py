import inflect

p = inflect.engine()
names = []
while True:
    try:
        name = input("Name: ").title()
        if name != "":
            names.append(name)
        else:
            continue
    except EOFError:
        break
    
print("Adieu, adieu, to " + p.join(names))