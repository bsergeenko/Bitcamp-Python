letter_month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").title()
        if "/" in date:
            month, day, year = date.split("/")
            day = int(day) 
            year = int(year)
            month = int(month)
            if day < 32 and month < 13:
                print(f"{year}-{month:02}-{day:02}")
        elif "," in date:
            month, day, year = date.replace(",", "").split(" ")
            day = int(day) 
            year = int(year)
            month = letter_month.index(month) + 1
            if day < 32 and month < 13:
                print(f"{year}-{month:02}-{day:02}")
        else:
            continue
    except ValueError:
        pass