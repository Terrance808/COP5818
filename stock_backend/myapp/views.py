from django.shortcuts import render

# Create your views here.
import yfinance as yf
from django.http import JsonResponse
import json

def get_stock_data(request): #, stockTickerInput):
    # ticker = yf.Ticker(stockTickerInput)
    # data = ticker.info
    # return JsonResponse(data)
    print("Request", request)
    # print("Data Pull", data)


def post_stock_data(request):
    if request.method == "POST":
        data = json.loads(request.body)
        ticker_symbols = data.get('tickers', [])
        stock_data = {}
        for symbol in ticker_symbols:
            ticker = yf.Ticker(symbol)
            stock_data[symbol] = ticker.info
        return JsonResponse(stock_data)
    return JsonResponse({"error" : "Invalid request"}, status=400)