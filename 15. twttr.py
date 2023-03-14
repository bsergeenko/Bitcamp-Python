text = input("Text: ")
vowels = ("aeiou")

for char in text.lower():
    if char in vowels:
        text = text.replace(char, "")
print(text)