from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class TaskLog(models.Model):
    name = models.CharField(max_length=70)
    status = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.status}"
