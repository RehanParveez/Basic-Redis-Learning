# from django.urls import path
# from main.views import time_view, products_view

# urlpatterns = [
#     path('timeview/', time_view),
#     path('productsview/', products_view),
# ]


# from django.urls import path
# from main.views import TaskListApiView

# urlpatterns = [
#     path('tasklist/', TaskListApiView.as_view()),
# ]

from django.urls import path
from main.views import TaskListCreateView, TaskDetailView, TestCeleryView, TestRetryTaskView, TestRetryLogTaskView
 

urlpatterns = [
    path('tasklist/', TaskListCreateView.as_view()),
    path('taskdetail/<int:pk>/', TaskDetailView.as_view()),
    # celery testing url
    path('testcelery/', TestCeleryView.as_view()),
    path('testretrycelery/', TestRetryTaskView.as_view()),
    path('testretrylogcelery/', TestRetryLogTaskView.as_view()),
]



