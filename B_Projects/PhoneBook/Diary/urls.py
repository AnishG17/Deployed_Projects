from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path('', views.save, name='save'),
    path('save/', views.save, name='save'),
    path('index/', views.index, name='index'),
    path('<int:id>/update/', views.update, name='update'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('search',views.search,name='search')
]