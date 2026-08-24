import requests
import sys

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=e51e8b62f450e4b63b126a6b4b2b3764b955135626df03c2e02f2457b448366f"

try:
    response = requests.get(url)
    json = response.json()
    data = json["data"]
except requests.RequestException:
    print(f"Error: {response.status_code}")


try:
    conversion = float(data["priceUsd"])
    usd = float(sys.argv[1])
    amount = conversion * usd
    print(f"${amount:,.4f}")
except ValueError:
    sys.exit("Error")


