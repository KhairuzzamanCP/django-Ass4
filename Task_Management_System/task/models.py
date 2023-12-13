from django.db import models
from category.models import Category

# Create your models here.

class TaskModel(models.Model):
    taskTitle  = models.CharField(max_length= 100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    Task_AssignDate = models.DateField()
    Categories = models.ManyToManyField(Category)
    def __str__(self):
      return self.taskTitle