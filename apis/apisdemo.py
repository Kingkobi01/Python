import requests, pprint,  json



def getPrice(symbol):
    url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

    params = {
        'symbol': symbol,
    }

    headers = {
        'Accepts': "application/json",
        'X-CMC_PRO_API_KEY':'236aa30c-8d7f-4245-8e91-67efb0057f0f'
    }
    response = requests.get(url, params=params, headers=headers)


    quote = response.json()['data'][symbol][0]['quote']['USD']['price']

    # .get('BTC', {})['quote']
    return quote

symbol = input("Give me a Cryptocurrency Symbol: ")

symbol = symbol.upper()

price = getPrice(symbol)

print(f"THe price of {symbol} is ${price}")

# # pprint.pprint(quote)
# jsonData = json.dumps(quote, indent=3)


# with open("crypto.json", 'w') as jsonFile:
#     jsonFile.write(jsonData)


# i

