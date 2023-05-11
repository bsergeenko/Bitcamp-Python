import sys

count = 0
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")
else:
    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                if not line.lstrip().startswith("#") and not line.isspace():
                    count += 1
            print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")