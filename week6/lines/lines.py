import sys

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    f_name = sys.argv[1]
    if not f_name.endswith(".py"):
        sys.exit("Not a Python file")
        
    try:
        with open(f_name) as file:
            lines_of_code = 0
            for line in file:
                line = line.strip()
                if not line.startswith("#") and line != "":
                    lines_of_code += 1
            print(lines_of_code)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
