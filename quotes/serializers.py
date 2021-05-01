from rest_framework import serializers
from quotes.models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    # Auto-generated data not needed by the client
    id = serializers.IntegerField(write_only=True, required=False)
    created_date = serializers.DateTimeField(write_only=True, required=False)
    modified_date = serializers.DateTimeField(write_only=True, required=False)

    class Meta:
        model = Quote
        fields = ('__all__')

    def create(self, validated_data):
        # Check if quote exists with the (from_currency_code and to_currency_code) identifiers  or create it if it does not exist
        bank_account, _ = Quote.objects.update_or_create(
            from_currency_code=validated_data.get('from_currency_code'),
            to_currency_code=validated_data.get('to_currency_code'),
            defaults={**validated_data})
        return bank_account
