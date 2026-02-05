from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
import datetime

# Create your views here.

def time_view(request):
    cached_time = cache.get("redis_time")

    if cached_time:
        return JsonResponse({"source": "redis", "time": cached_time})
    present_time = str(datetime.datetime.now().time())
    cache.set("redis_time", present_time, timeout=14)

    return JsonResponse({"cached": False, "time": present_time})

def products_view(request):
    products = cache.get("redis_products")

    if products:
        return JsonResponse({"cached": True, "products": products})
    products = ["laptop", "bulb", "magnet"]
    cache.set("redis_products", products, timeout=25)

    return JsonResponse({"cached": False, "products": products})

