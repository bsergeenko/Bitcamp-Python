import sys

count = 0
try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py"):
        with open(sys.argv[1], "r") as file:
            lines = file.readline()
            for line in file:
                if line.startswith("#") or line =="\n":
                    continue
                else:
                    count += 1
            print(count)
    else:
        print("Not a python file")
except FileNotFoundError:
    print("File does not exist")