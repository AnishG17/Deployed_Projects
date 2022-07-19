from django.urls import path
from todoList import views
urlpatterns = [
    path('',views.index,name='index'),
]
