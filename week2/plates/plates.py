def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    num_used = False
    if len(s) < 2 or len(s) > 6:
        return False
    if not s.isalnum():
        return False
    if not s[0].isalpha() and not s[1].isalpha():
        return False
    for c in s:
        if c.isdigit():
            if num_used == False:
                if c == "0":
                    return False
            num_used = True
        else:
            if num_used:
                return False
    return True

if __name__ == "__main__":
    main()
    