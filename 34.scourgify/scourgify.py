import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
    sys.exit("Not a CSV file")

students = []
try:
    with open(sys.argv[1]) as before:
        reader = csv.DictReader(before)
        for row in reader:
            first, last = row["name"].split(",")
            students.append({"first": first.strip(), "last": last, "house": row["house"]})
except:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w") as after:
    writer = csv.DictWriter(after, fieldnames = ['first', 'last', 'house'])
    writer.writeheader()
    for row in students:
        writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})