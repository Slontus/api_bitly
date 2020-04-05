import requests
import os
import argparse
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("ACCESS_TOKEN")
URL_BITLINK = "https://api-ssl.bitly.com/v4/bitlinks"
URL_CLICKS_SUMMARY = ("https://api-ssl.bitly.com/v4/bitlinks/", "/clicks/summary")


def shorten_link(token, url):
    body = {'long_url': url}
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(URL_BITLINK, json=body, headers=headers)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token, bitlink):
    payload = {'unit': 'day', 'units': -1}
    headers = {'Authorization': f'Bearer {token}'}
    link = bitlink.join(URL_CLICKS_SUMMARY)
    response = requests.get(link, params=payload, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def create_parser():
    parser = argparse.ArgumentParser(description='Program returns short biy.ly link in case if long link provided '
                                                 'and quantity of clicks in case if bit.ly link provided')
    parser.add_argument('-l', '--link', help='url link')
    return parser


def main(link):
    if link.startswith('bit.ly/'):
        try:
            clicks_count = count_clicks(TOKEN, link)
        except requests.exceptions.HTTPError as error:
            print(f"Bitlink incorrect:\n{error}")
        else:
            print(f"Clicks count for {link}: {clicks_count}")
    else:
        try:
            bitlink = shorten_link(TOKEN, link)
        except requests.exceptions.HTTPError as error:
            print(f"Link is not correct:\n{error}")
        else:
            print('Generated bitlink:', bitlink)


if __name__ == "__main__":
    parser = create_parser()
    argument = parser.parse_args()
    if argument.link:
        main(argument.link)
    else:
        main(input('link: '))
