def main():
    text = input("Input: ")
    print("Output:",shorten(text))




def shorten(word):
    output = ""
    for letter in word:
        if ("a" == letter.lower() or "e" == letter.lower() or "i" == letter.lower() or "o" == letter.lower() or "u" == letter.lower()):
            continue
        output += letter
    return output


if __name__ == "__main__":
    main()

