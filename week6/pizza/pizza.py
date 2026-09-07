import tabulate
import sys
import csv

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments" if len(sys.argv)<2 else "Too many command-line arguments")

file_name = sys.argv[1]

if not file_name.endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    table = []
    with open(file_name) as file:
        reader = csv.reader(file)
        headers = next(reader)
        for line in reader:
            table.append(line)
        print(tabulate.tabulate(table, headers, tablefmt ="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
