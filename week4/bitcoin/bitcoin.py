import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    API_KEY = "865ba8a619f31e0b3f8240f976bf26ae920d25b83587c985a437a42989014fe7"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price_usd = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Network or API error")

    cost = bitcoins * price_usd
    print(f"${cost:,.4f}")

if __name__ == "__main__":
    main()

