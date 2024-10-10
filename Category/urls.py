from django.urls import path
from Category import views

urlpatterns = [
    path('', views.category, name='add_category'),  # This renders 'add_task.html'
]
