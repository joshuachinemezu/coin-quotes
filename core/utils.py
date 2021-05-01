import re
from django.conf import settings
import requests


def fetch_quotes():
    response = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=%s' %
                            (getattr(settings, 'ALPHAVANTAGE_API_KEY', None)))
    return response.json()


def parse_key(string):
    """Parse keys of alpahvantage response and remove unaccepted characters."""
    string = string.replace(" ", "")  # Remove whitespaces
    string = string[string.find('.')+1:]  # Remove all characters before '.'

    # Convert string to camel case
    string = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()

    # Remove duplicate of '_'
    return remove_duplicates(string, '_')


def remove_duplicates(s, needle):
    """Scan through string looking for a match to the needle and remove it's duplicates."""
    pattern = "(?P<char>[" + re.escape(needle) + "])(?P=char)+"
    return re.sub(pattern, r"\1", s)
