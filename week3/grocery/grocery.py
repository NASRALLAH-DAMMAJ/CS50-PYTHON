def main():
    list = {}
    while 1:
        try:
            item = input().upper().strip()
            if not item == "":
                if (item in list):
                    list[item] += 1
                else:
                    list[item] = 1


        except(KeyError):
            pass


        except(EOFError):
            for i , c  in sorted(list.items()):
                print(c, i)
            break

main()