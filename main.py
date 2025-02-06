import requests
from secret_keys import currency_api_key
import pprint

API_KEY = currency_api_key  # enter your api key here


def main():

    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    currencies = list(data["data"].keys())

    to_convert = currency_input("Choose currency to convert:", currencies)
    amount = amount_input("How much of the currency?")
    print()
    convert_to = currency_input(f"Choose currency to convert {amount} {to_convert} to:", currencies)

    print()
    exchange_rate = data["data"][convert_to]/data["data"][to_convert]
    print(f"{amount} {to_convert} = {round(exchange_rate * amount, 3)} {convert_to}\n")


def currency_input(prompt, currencies):
    print(prompt)
    pprint.pp(currencies, width=30, compact=True)
    while True:
        currency = input().upper()
        if currency in currencies:
            return currency
        else:
            print("Invalid currency")


def amount_input(prompt):
    print(prompt)
    while True:
        amount = input()
        try:
            amount = float(amount)
            return amount
        except ValueError:
            print("Invalid amount")
        

main()
