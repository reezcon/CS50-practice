import sys
import csv

if len(sys.argv) !=3:
    sys.exit("Too few command-line arguments" if len(sys.argv)<3 else "Too many command-line arguments")

path_before = sys.argv[1]
path_after = sys.argv[2]

if path_before.endswith(".csv") and path_after.endswith(".csv"):
    try:
        with open(path_before) as input_file, open(path_after, "w", newline="") as output_file:
            reader = csv.DictReader(input_file)
            writer = csv.DictWriter(output_file, fieldnames = ["first", "last", "house"])

            # Writing to output file
            writer.writeheader()
            for row in reader:
                last_name, first_name = row["name"].split(", ")
                house = row["house"]
                writer.writerow({"first": first_name, "last": last_name, "house": house})

    except:
        sys.exit(f"Could not read {path_before}")
else:
    sys.exit("Not a .csv file")
