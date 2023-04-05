import sys
import csv

try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):

        with open(sys.argv[1]) as before:
            reader = csv.DictReader(before)

            with open(sys.argv[2], "w", newline='') as after:
                    writer = csv.DictWriter(after, fieldnames = ['first', 'last', 'house'])
                    writer.writeheader()
                    for row in reader:
                        students = {}
                        first, last = row["name"].split(",")
                        house = row["house"]
                        writer.writerow({"first": first, "last": last, "house": house})
                
            
    else:
        sys.exit("Not csv file")


except FileNotFoundError:
    print("File does not exist")