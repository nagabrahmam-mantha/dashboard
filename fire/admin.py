from django.contrib import admin
from .models import Account, Asset, Country, Ticker, Transaction, Dividend

admin.site.register(Account)
admin.site.register(Asset)
admin.site.register(Country)
admin.site.register(Ticker)
admin.site.register(Transaction)
admin.site.register(Dividend)
