from django.db import models
from Category.models import CategoryModel

class TaskModel(models.Model):
    title =models.CharField(max_length=150)
    task_description =models.TextField()
    is_completed = models.BooleanField(default=False)
    Task_assign_date =models.DateField()
    
    categories = models.ManyToManyField(CategoryModel, related_name='tasks')  # Create Many-to-Many relationship
    
    def __str__(self):
        return  self.title