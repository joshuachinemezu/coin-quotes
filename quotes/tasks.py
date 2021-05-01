from celery.utils.log import get_task_logger
from celery import shared_task
from core.utils import fetch_quotes, parse_key
from quotes.serializers import QuoteSerializer


logger = get_task_logger(__name__)


@shared_task
def save_currency_quotes():
    logger.info('Running Currency Quotes Saving Task')

    # Fetch result from alphavantage
    response = fetch_quotes()

    # Clean up data
    currency_quote = response['Realtime Currency Exchange Rate']
    for key in list(currency_quote):
        new_key_name = parse_key(key)
        currency_quote[new_key_name] = currency_quote.pop(key)

    # Update our datastore
    quotes_serializer = QuoteSerializer(
        data=currency_quote)
    if quotes_serializer.is_valid():
        quotes_serializer.save()

    return 'Ok'
