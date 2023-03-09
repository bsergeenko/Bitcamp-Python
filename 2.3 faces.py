def main():
    hello = input("something: ")
    print (convert(hello))



def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")


main()