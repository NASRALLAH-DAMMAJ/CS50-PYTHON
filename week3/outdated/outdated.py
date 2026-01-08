def main():
    mounths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while 1:
        date = input("Date: ").strip()
        try:
            if "/" in date:
                m, d, y = date.split("/")
                m = int(m)
                d = int(d)
                y = int(y)

            else:
                m, d, y = date.split(" ")
                d = d.replace(",","")
                d = int(d)
                y = int(y)
            
                if m in mounths:
                    m = mounths.index(m) + 1
                else:
                    continue
        except(ValueError):
            continue

        if m > 12 or d > 31 or len(str(y)) > 4:
            continue
        
        if m == 0 or d == 0 or y == 0:
            continue
        
        print(f"{y:04}-{m:02}-{d:02}")
        break

main()
