import json
from urllib import parse
import requests

def read_bing_key():
    bing_api_key = None

    try:
        with open('bing.key', 'r') as f:
            bing_api_key = f.readline()
    except:
        raise IOError('bing.key file not found')

    return bing_api_key


def run_query(search_terms):
    bing_api_key = read_bing_key()

    if not bing_api_key:
        raise KeyError('Bing Key Not Found')

    root_url = 'https://api.datamarket.azure.com/Bing/Search/'
    service = 'Web'

    results_per_page = 10
    offset = 0

    query = "'{0}'".format(search_terms)

    query = parse.quote(query)

    search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
                    root_url,
                    service,
                    results_per_page,
                    offset,
                    query)

    results = []

    try:
        r = requests.get(search_url, auth=("", bing_api_key))
        json_response = json.loads(r.text)
        print(json_response)
        for result in json_response['d']['results']:
            results.append({'title': result['Title'], 'link': result['Url'], 'summary': result['Description']})
    except:
        print('Error when querying the Bing API')

    return results


def main():
    run_query(input())


if __name__ == '__main__':
    main()

































