from django.urls import include, path
from calorie import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('',views.delete,name='delete')
    path('delete/<int:id>/', views.delete, name="delete"),
    ]