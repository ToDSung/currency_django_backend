from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.apps import apps

from currency_data.models import JPY, CNY, USD, EUR, GBP, AUD, SGD

# Create your views here.
# api

def get_currency_list(request):
    currency_list = [ i for i in apps.all_models['currency_data']]
    return JsonResponse({'currencies': currency_list})

def get_currency_data(request, item):
    currency_list = [ i for i in apps.all_models['currency_data']]
    temp_dict = { 'jpy': [JPY, '日圓'], 'cny': [CNY, '人民幣'], 'usd': [USD, '美金']
                , 'eur': [EUR, '歐元'], 'gbp': [GBP, '英鎊'], 'aud': [AUD, '澳幣']
                , 'sgd': [SGD, '新加坡元']}
    
    if item in currency_list:
        currency_object = temp_dict[item][0]
        all_curency_info = currency_object.objects.all()
        data_dict = {}
        data_dict['currency_eng'] = item.upper()
        data_dict['currency_chn'] = temp_dict[item][1]
        for row in all_curency_info:
            data_dict[int(row.id)] = {
            "date": row.date,
            "rate_cash_buy": row.rate_cash_buy, 
            "rate_cash_sell": row.rate_cash_sell, 
            "rate_sight_buy": row.rate_sight_buy,
            "rate_sight_sell" :row.rate_sight_sell
            }
        return JsonResponse(data_dict)
    else: 
        return JsonResponse(data={'http_code': '404 no match currency'},  status=404)
