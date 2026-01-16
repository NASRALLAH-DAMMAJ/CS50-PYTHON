import requests
import sys

def main():
    if (len(sys.argv) < 2):
        sys.exit("Missing command-line argument")

    number_of_bitcoins = sys.argv[1]
    if number_of_bitcoins.isalpha():
        sys.exit("Command-line argument is not a number")

    try:
        res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        res = res.json()
        rate = res['bpi']['USD']['rate_float']
    
        cost = rate * float(number_of_bitcoins)
        output = "$"+"{:,}".format(cost)

        print(output)

    except:
        sys.exit("Check your internet connection")

if __name__ == "__main__":
    main()
