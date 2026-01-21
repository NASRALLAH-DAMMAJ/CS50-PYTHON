import random
import sys


def main():
    level = get_level()

    n = 0
    errors = 0
    score = 0
    
    while 1:
        if (n < 10):
            x = generate_integer(level)
            y = generate_integer(level)
            z = x + y
            while 1:
                try:
                    user = int(input(f"{x} + {y} = "))
                    if (user != z):
                        raise ValueError
                    else:
                        n += 1
                        score += 1
                        break

                except (ValueError):
                    print("EEE")
                    errors += 1
                    if errors >= 3:
                        print(f"{x} + {y} = {z}")
                        errors = 0
                        n += 1
                        break
        elif (n == 10):
            print(f"Score: {score}")
            sys.exit(0)
        else:
            sys.exit(0)
            

                        




    


def get_level():
    while 1:
        try:
            Level = int(input("Level: "))
            if (1 <= Level <= 3):
                return Level
            else:
                raise ValueError
             
        except (ValueError):
            continue



def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    else:  # level == 3
        n = random.randint(100, 999)
    return n



if __name__ == "__main__":
    main()