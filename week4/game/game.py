import random
import sys

def main():
    while 1:
        try:
            level = int(input("Level: "))
            if level <= 0:
                continue
            else:
                num = random.randrange(1, level)
                break
        except (ValueError):
            continue
        

    while 1:
        try:
            guass = int(input("Guass: "))
        except (ValueError):
            continue

        if guass <= 0:
            continue

        if guass < num:
            print("Too small!")
            continue
        elif guass > num:
            print("Too large!")
            continue
        else:
            sys.exit("Just right!")
            



if __name__ == "__main__":
    main()
