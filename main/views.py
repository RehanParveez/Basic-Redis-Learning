# from django.shortcuts import render
# from django.http import JsonResponse
# from django.core.cache import cache
# import datetime

# # Create your views here.

# def time_view(request):
#     cached_time = cache.get("redis_time")

#     if cached_time:
#         return JsonResponse({"source": "redis", "time": cached_time})
#     present_time = str(datetime.datetime.now().time())
#     cache.set("redis_time", present_time, timeout=14)

#     return JsonResponse({"cached": False, "time": present_time})

# def products_view(request):
#     products = cache.get("redis_products")

#     if products:
#         return JsonResponse({"cached": True, "products": products})
#     products = ["laptop", "bulb", "magnet"]
#     cache.set("redis_products", products, timeout=25)

#     return JsonResponse({"cached": False, "products": products})





# Redis with DRF Learning

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.core.cache import cache
# from main.models import Task
# from main.serializers import TaskSerializer
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from django.views import View
# from django.http import JsonResponse
# from main.tasks import practice_background_task, practice_retry_task, practice_retry_log_task, calculate_task_result
# from celery.result import AsyncResult  # related to getcalculatetaskresultview


# class TaskListApiView(APIView):
#     def get(self, reuqest):
#         cache_key = 'task_list_data'
        
#         cached_data = cache.get(cache_key)
#         if cached_data:
#             return Response({'source':'cache', 'data':cached_data})
        
#         queryset = Task.objects.all()
#         serializer = TaskSerializer(queryset, many=True)
#         cache.set(cache_key, serializer.data, timeout=50)
#         return Response({'source':'database', 'data':serializer.data})
    
    
# Use of ListCreateAPIView

# class TaskListCreateView(ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

#     def list(self, request, *args, **kwargs):
#         cache_key = "task_list"

#         cached_data = cache.get(cache_key)
#         if cached_data:
#             return Response({"source": "cache", "data":cached_data})

#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)

#         cache.set(cache_key, serializer.data, timeout=60)

#         return Response({"source": "database", "data": serializer.data})
    
#     # the invalidation logic
#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#         cache.delete("task_list")
#         return response
    
# class TaskDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    
#     def update(self, request, *args, **kwargs):
#         response = super().update(request, *args, **kwargs)
        
#         # invalidating the cache after delete
#         cache.delete("task_list")
#         return response
    
#     def destroy(self, request, *args, **kwargs):
#         response = super().destroy(request, *args, **kwargs)
        
#         # invalidating the cache after delete
#         cache.delete()
#         return response

# class TestCeleryView(View):
#     def get(self, request, *args, **kwargs):
#         practice_background_task.delay()
#         return JsonResponse({"status": "the task has been sent to the celery"})

# class TestRetryTaskView(View):
#     def get(self, request, *args, **kwargs):
#         practice_retry_task.delay()
#         return JsonResponse({"status": "the retry task has been sent to the celery"})

# class TestRetryLogTaskView(View):
#     def get(self, request, *args, **kwargs):
#         practice_retry_log_task.delay()
#         return JsonResponse({"status": "the retry task with the db logging has been sent to the celery"})
    
# class TestCalculateTaskView(View):
#     def get(self, request, *args, **kwargs):
#         number = int(request.GET.get('number', 5))
#         task = calculate_task_result.delay(number)
#         return JsonResponse({'status':'task sent', 'task_id': task.id})
   
   
# not required
 
# class GetCalculateTaskResultView(View):
#     def get(self, request, *args, **kwargs):
#         task_id = request.GET.get('task_id')
#         task_result = AsyncResult(task_id)
#         if task_result.ready():
#             return JsonResponse({'status':'done', 'result':task_result.result})
#         return JsonResponse({'status':'pending'})
        

# celery-beat realted practice views

from django.views import View
from django.http import JsonResponse
from django.core.cache import cache
from main.tasks import heartbeat_task, clear_task

class HeartbeatView(View):
    def get(self, request):
        heartbeat_task.delay()
        return JsonResponse({'status': 'heartbeat is triggered manually'})
    
class LastBeatTimestampView(View):
    def get(self, request):
        timestamp = cache.get("last_beat_run")
        return JsonResponse({"last_beat_run": timestamp})

class ClearTaskListView(View):
    def get(self, request):
        clear_task.delay()
        return JsonResponse({"status": "task_list cache clear task sent"})
    
