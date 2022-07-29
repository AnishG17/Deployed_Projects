
from django.urls import path
# from . import views
from yt_app import views
urlpatterns = [
    path('', views.youtube, name='youtube'),
]
