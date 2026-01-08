def main():
    cent = 50
    while (cent > 0):
        print(f"Amount Due: {abs(cent)}")
        try:
            coin = int(input("Insert Coin: "))
        except(ValueError):
            continue
        if (coin == 25 or coin == 10 or coin == 5):
            cent -= coin
        if cent <= 0:
            break
    print(f"Change Owen: {abs(cent)}")
        
    
main()