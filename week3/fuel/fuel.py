def main():
    while 1:
        try:
            fraction = input("Fraction: ").split("/")
            x, y = fraction
            x, y = int(x), int(y)
            int_percentage = round((x / y) * 100)
            percentage = str(int_percentage) + "%"
            if (int_percentage >= 99):
                if (int_percentage > 100):
                    continue
                else:
                    percentage = "F"
            elif (int_percentage <= 1):
                percentage = "E"
            print(percentage)
            break
        except(ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
    