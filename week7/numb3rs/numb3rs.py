import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))
    sys.exit()


def validate(ip):
    try:
        if (eq(ip, 0) and eq(ip, 1) and eq(ip, 2) and eq(ip, 3)):
            return True
        else:
            return False
    except (ValueError, IndexError):
        return False



def eq(ip, num):
    if (ip.split(".")[num].startswith("0")):
        if (int(ip.split(".")[num]) == 0):
            pass
        else:
            return False
    if not (255 >= int(ip.split(".")[num]) >= 0):
        return False
    return True

if __name__ == "__main__":
    main()