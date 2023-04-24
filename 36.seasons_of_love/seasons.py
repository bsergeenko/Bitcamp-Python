from datetime import date
import datetime
import inflect


def main():
    try:
        birthday = input("Your Birthday: ")
        print(minutes_to_words(minutes(birthday)), "minutes")
    except ValueError:
        print("Invalid date")

def minutes(birthday, today = date.today()):
    birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    age_in_minutes = (today - birthday.date()).total_seconds() // 60
    return int(age_in_minutes)

def minutes_to_words(minutes):
    p = inflect.engine().number_to_words(f"{minutes}", andword="")
    
    return p


if __name__ == "__main__":
    main()