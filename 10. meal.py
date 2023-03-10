time = input("what time is it? ")
hours, minutes = time.split(":")
if hours == "7" or hours == "8" and minutes == "00":
    print("breakfast time")
elif hours == "12" or hours == "13" and minutes == "00":
    print("lunch time")
elif hours == "18" or hours == "19" and minutes == "00":
    print("dinner time")
else:
    print("")