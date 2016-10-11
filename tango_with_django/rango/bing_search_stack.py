from urllib.parse import quote_plus
import json
import requests


def bing_search(query):
    # Your base API URL
    with open('bing.key', 'r') as f:
        azure_primary_key = f.readline()
    url = "https://api.datamarket.azure.com/Bing/Search/v1/Web"

    # Query parameters. Don't try using urlencode here.
    # Don't ask why, but Bing needs the "$" in front of its parameters.
    # The '$top' parameter limits the number of search results.
    url += "?$format=json&$top=10&Query=%27{}%27".format(quote_plus(query))

    # You can get your primary account key at https://datamarket.azure.com/account
    r = requests.get(url, auth=("", azure_primary_key))
    resp = json.loads(r.text)
    print(url)
    return (resp)

if __name__ == '__main__':
    a = bing_search(input())
    print(a)