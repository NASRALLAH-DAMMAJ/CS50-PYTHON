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
        else:
            sys.exit(f"Score: {score}")
            

                        




    


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
    n = random.randint(0, ((level * 10) - 1))
    return n



if __name__ == "__main__":
    main()