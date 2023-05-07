from django.shortcuts import render
from .models import Transaction, Ticker
from .plotly_plot import *

def index(request):
    transactions_ticker = Transaction.objects.values_list('ticker__name', 'quantity').distinct()

    trans = {}
    for transaction in transactions_ticker:
        symbol = transaction[0]
        quantity = transaction[1]

        if symbol in trans:
            trans[symbol] += quantity
        else:
            trans[symbol] = quantity

    target_plot = plotly_plot(list(trans.values()), list(trans.keys()))

    context = {
        'target_plot': target_plot,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
