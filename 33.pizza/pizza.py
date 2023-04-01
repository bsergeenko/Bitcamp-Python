import sys
import csv
from tabulate import tabulate

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv"):
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            pizzas = []

            for row in reader:
                pizzas.append(row)

        table = pizzas[1:]
        headers = pizzas[0]
                
        print(tabulate(table, headers, tablefmt="grid"))
    else:
        sys.exit("Not csv file")

except FileNotFoundError:
    print("File does not exist")