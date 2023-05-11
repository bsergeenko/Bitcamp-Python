def main():
    time = convert(input("what time is it? "))
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        print("")

def convert(time):
    hour, min = time.split(":")
    hour = float(hour)
    min = float(min) / 60
    time = hour + min
    return time

main()