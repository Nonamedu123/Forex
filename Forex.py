import requests
import json

def get_crypto_price(symbol):
    base_url = "https://api.binance.com/api/v3/ticker/price"
    params = {"symbol": symbol}

    response = requests.get(base_url, params=params)
    data = response.json()

    if "price" in data:
        return data["price"]
    else:
        return None

if __name__ == "__main__":
    crypto_symbol = "BTCUSDT"  # Przykład: cena Bitcoina w USD
    price = get_crypto_price(crypto_symbol)

    if price:
        print(f"Aktualna cena {crypto_symbol}: {price}")
    else:
        print("Nie udało się pobrać danych.")
