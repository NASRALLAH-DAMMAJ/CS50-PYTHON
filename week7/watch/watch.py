import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matchs := re.search(r'<iframe(?:.+)?src="https?://(?:www.)youtube.com/embed/(.+)"((?: title=)(?:.+))?></iframe>', s):
        return f"https://youtu.be/{matchs.group(1)}"
    else:
        return None





if __name__ == "__main__":
    main()