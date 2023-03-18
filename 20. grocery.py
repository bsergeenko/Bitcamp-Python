grocery_list = {}
while True:
    try:
        item = input("").upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
        
    except EOFError:
        break

sorted_list = sorted(grocery_list)
for item in sorted_list:
    print (grocery_list[item], item)