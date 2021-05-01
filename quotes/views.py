from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.response import Response
from core.response import HttpRes
from quotes.models import Quote
from quotes.serializers import QuoteSerializer
from core.utils import fetch_quotes, parse_key
from django.shortcuts import get_object_or_404

response_format = HttpRes().response


class QuoteView(APIView):
    permission_classes = [HasAPIKey]
    serializer_class = QuoteSerializer

    def post(self, request):
        # Fetch result from alphavantage
        response = fetch_quotes()

        # Clean up data
        currency_quote = response['Realtime Currency Exchange Rate']
        for key in list(currency_quote):
            new_key_name = parse_key(key)
            currency_quote[new_key_name] = currency_quote.pop(key)

        # Update datastore
        quotes_serializer = self.serializer_class(
            data=currency_quote)
        if quotes_serializer.is_valid():
            # We can move this operation to a redis server
            quotes_serializer.save()

        response_format['data'] = currency_quote
        response_format['message'] = 'Operation was successful'
        return Response(response_format)

    def get(self, request):

        quote = get_object_or_404(Quote, from_currency_code='BTC')
        quote_serializer = self.serializer_class(quote)

        response_format['data'] = quote_serializer.data
        response_format['message'] = 'Operation was successful'
        return Response(response_format)
