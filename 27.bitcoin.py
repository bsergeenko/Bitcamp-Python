import sys
import requests

try:
    bitcoin = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    usd = float((response.json()['bpi']['USD']['rate']).replace(",", ""))
    amount = bitcoin * usd

    print(f"${amount:,.4f}")
    
except requests.RequestException:
    pass

    