from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=200, help_text='Enter an account name')
    number = models.CharField(max_length=200, help_text='Enter an account number')
    broker = models.CharField(max_length=200, help_text='Enter an account broker')
    type = models.CharField(max_length=200, help_text='Enter an account type (Ex: Margin, TFSA)')

    STATUS = (('live', 'Live'), ('demo', 'Demo'))
    status = models.CharField(max_length=5, choices=STATUS, blank=False, default='Live', help_text='Live or Demo')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Asset(models.Model):
    type = models.CharField(max_length=200, help_text='Enter asset type (Ex: Stock, ETF)')

    def __str__(self):
        """String for representing the Model object."""
        return self.type

class Country(models.Model):
    name = models.CharField(max_length=200, help_text='Enter country (Ex: Canada, USA)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Ticker(models.Model):
    name = models.CharField(max_length=200, help_text='Enter ticker (Ex: MSFT, AMZN)')
    description = models.CharField(max_length=200, help_text='Enter description')
    sector = models.CharField(max_length=200, help_text='Enter sector')
    asset = models.ForeignKey(Asset, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(help_text='Enter current price')
    dividend_yield_amount = models.FloatField('Dividend Yield (Amount)', help_text='Enter dividend yield (Amount)')
    dividend_yield_percentage = models.FloatField('Dividend Yield (Percentage)', help_text='Enter dividend yield (Percentage)')
    currency = models.CharField(max_length=200, help_text='Enter currency (Ex: CAD, USD)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Transaction(models.Model):
    ticker = models.ForeignKey(Ticker, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField(help_text='Enter quantity')
    date_time = models.DateTimeField('Date Time', help_text='Enter datetime')
    entry_price = models.FloatField('Entry Price', help_text='Enter entry price')
    commission = models.FloatField(help_text='Enter commission')
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return str(self.ticker)

class Dividend(models.Model):
    ticker = models.ForeignKey(Ticker, on_delete=models.SET_NULL, null=True)
    date = models.DateField(help_text='Enter date')
    amount = models.FloatField(help_text='Enter amount')
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.account
