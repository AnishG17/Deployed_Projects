from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
  
urlpatterns = [
    path('',views.counter1, name='counter1'),
    # path('admin/', admin.site.urls),
]