from django.contrib import admin
from main.models import Task, TaskLog

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed']
    
@admin.register(TaskLog)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'message', 'created_at']