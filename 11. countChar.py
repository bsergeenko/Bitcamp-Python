text = input ("please whrite the text: ")
if text == "":
    text2 = input ("It is necessery to write the text: ")
    print (text2, "has", len(text2), "charackter")
else:
    print (text, "has", len(text), "charackter")