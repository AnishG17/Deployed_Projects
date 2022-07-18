from django.urls import path
from napp import views
urlpatterns = [
path('', views.index, name ='index'),
	
]