import sys
from pyfiglet import Figlet

def main():
    fig = Figlet()

    if (len(sys.argv) == 1):
        pass
    elif (len(sys.argv) == 3 and sys.argv[1] == "-f"):
        try:
            fig = Figlet(font=sys.argv[2])
        except (Exception):
            sys.exit(1)
    else:
        sys.exit(1)
    

    text = input().strip()
    print(fig.renderText(text))


if __name__ == "__main__":
    main()