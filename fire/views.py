from django.shortcuts import render
from .models import Transaction, Ticker
from .plotly_plot import *

def get_avg_price(key, transaction_dict):
    unique_values = Transaction.objects.values_list(key, flat=True).distinct()

    for value in unique_values:
        count = Transaction.objects.filter(**{key: value}).count()
        transaction_dict[value] = transaction_dict[value] / count

    return transaction_dict

def index(request):
    transactions_ticker = Transaction.objects.values_list('ticker__name', 'quantity', 'entry_price')

    trans = {}
    for transaction in transactions_ticker:
        symbol = transaction[0]
        quantity = transaction[1]
        price = transaction[2]

        if symbol in trans:
            trans[symbol] += (quantity*price)
        else:
            trans[symbol] = (quantity*price)

    trans = get_avg_price("ticker__name", trans)

    target_plot = plotly_plot(list(trans.values()), list(trans.keys()))

    context = {
        'target_plot': target_plot,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
