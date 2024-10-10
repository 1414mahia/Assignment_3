from django.urls import path
from Task import views

urlpatterns = [
    path('', views.task, name='add_task'),  # This renders 'add_task.html'
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
]
