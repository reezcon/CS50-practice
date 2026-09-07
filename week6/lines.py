import sys

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")

file_name = sys.argv[1]

if not file_name.endswith(".py"):
    sys.exit("Not a Python file")
try:
    count = 0
    with open(file_name) as file:
        for line in file:
            stripped = line.strip()
            if stripped == "":
                continue
            if stripped.startswith("#"):
                continue

            count+=1
    print(count)
except FileNotFoundError:
    sys.exit("File does not exist")


