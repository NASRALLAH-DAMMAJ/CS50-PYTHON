def main():
    file = input("File Name: ").strip().lower()

    if "." in file:
        extension = file.rsplit(".", 1)[1]
    else:
        extension = ""

    if extension == "gif" or extension == "png":
        print(f"image/{extension}")

    elif extension == "jpg" or extension == "jpeg":
        print("image/jpeg")

    elif extension == "pdf" or extension == "zip":
        print(f"application/{extension}")

    elif extension == "txt":
        print("text/plain")

    else:
        print("application/octet-stream")

main()
