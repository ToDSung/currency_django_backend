from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from currency_data.models import JPY

# Create your views here.
# api

def here(request):
    return HttpResponse('Hello World!')

def get_jpy_data(request):
    latest_data = JPY.objects.all()
    data_dict = {}
    data_dict['currency_eng'] = 'JPY'
    data_dict['currency_chn'] = '日圓'
    for q in latest_data:
        data_dict[int(q.id)] = {
        "date": q.date,
        "rate_cash_buy":q.rate_cash_buy, 
        "rate_cash_sell":q.rate_cash_sell, 
        "rate_sight_buy":q.rate_sight_buy,
        "rate_sight_sell":q.rate_sight_sell
        }
    print(data_dict)
    return JsonResponse(data_dict)