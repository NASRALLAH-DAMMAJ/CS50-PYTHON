import sys
import csv
from tabulate import tabulate

def main():

    if (len(sys.argv) < 2):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > 2):
        sys.exit("Too many command-line arugments")

    csv_file = sys.argv[1]
    if not csv_file.endswith(".csv"):
        sys.exit("Not a CSV File")

    TABLE = []
    HEADERS = []
    try:
        with open(csv_file) as file:
            reader = csv.DictReader(file)
            HEADERS = reader.fieldnames
            for row in reader:
                value = list(row.values())
                TABLE.append(value)

        print(tabulate(TABLE, HEADERS, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
