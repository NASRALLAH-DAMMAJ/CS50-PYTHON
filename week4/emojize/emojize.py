import emoji

def main():
    text = input().strip()
    print(emoji.emojize(text, language="alias"))


if __name__ == "__main__":
    main()