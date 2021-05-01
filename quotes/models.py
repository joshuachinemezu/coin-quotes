from django.db import models


class Quote(models.Model):
    from_currency_code = models.CharField(max_length=100)
    from_currency_name = models.CharField(max_length=100)
    to_currency_code = models.CharField(max_length=100)
    to_currency_name = models.CharField(max_length=100)
    exchange_rate = models.CharField(max_length=100)
    last_refreshed = models.CharField(max_length=100)
    time_zone = models.CharField(max_length=100)
    bid_price = models.CharField(max_length=100)
    ask_price = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'quotes'
