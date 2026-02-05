from django.urls import path
from main.views import time_view, products_view

urlpatterns = [
    path('timeview/', time_view),
    path('productsview/', products_view),
]

