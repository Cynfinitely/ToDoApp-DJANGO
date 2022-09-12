from turtle import mode
from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200) #title for todo task
    created_date = models.DateTimeField(auto_now_add=True) # Date will be added
    complated = models.BooleanField(default=False) # When we finished the task, it will be overlined

    class Meta:
        ordering = ['-created_date',] #display the last created on top
    
    def __str__(self):
        return self.title
