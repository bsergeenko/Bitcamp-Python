text = input("camelCase: ")
text2 = ""
for character in text:
    if character.isupper():
        text2 += "_"
    text2 += character.lower()
print("snake_case: " + text2)