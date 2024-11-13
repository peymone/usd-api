from django.http import JsonResponse
from .models import Usd
import requests
from tzlocal import get_localzone

from datetime import datetime
from re import search


api_link = 'https://currencyapi.com/currency-conversion/usd-rub-1'
pattern = '\d{2}.\d{2} Russian Ruble'
time_format = '%d/%m/%Y %H:%M:%S'

def get_current_usd(request):
    
    # Get current 'usd to rub' exchange rate
    response = requests.get(api_link)
    match_obj = search(pattern, response.text)
    current_usd = match_obj.group(0).split()[0]
    
    # Save current usd to database
    usd = Usd(usd=float(current_usd))
    usd.save()
    
    # Get 10 last api responses from db and return it in json
    json_response = dict()
    select_last_10 = Usd.objects.all().order_by('-time')[:10]
    for exchange_rate in select_last_10.values():
        
        # Convert time in database from utc to local
        time_with_localzone = exchange_rate['time'].astimezone(get_localzone())
        formated_time = datetime.strftime(time_with_localzone, time_format)        
        
        json_response[formated_time] = exchange_rate['usd']
                
    return JsonResponse(json_response)