import sys
import csv
from tabulate import tabulate


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")

pizzas = []
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        for row in reader:
            pizzas.append(row)
        print(tabulate(pizzas[1:], headers = pizzas[0], tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")