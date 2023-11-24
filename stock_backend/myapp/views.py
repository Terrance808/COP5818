from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def post_stock_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            ticker_symbol = data['stock_ticker']

            if ticker_symbol:
                stock = yf.Ticker(ticker_symbol)
                try:
                    history = stock.history(period="1d")
                    closing_price = history['Close'].iloc[-1] if not history.empty else None
                    print(type(closing_price))
                    return JsonResponse({'status': 'success', 'ticker': ticker_symbol, 'current_price': closing_price})
                except Exception as e:
                    return JsonResponse({'status': 'error', 'message': f'Error fetching stock data: {e}'}, status=500)

            else:
                return JsonResponse({'status': 'error', 'message': 'Stock ticker symbol missing'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
