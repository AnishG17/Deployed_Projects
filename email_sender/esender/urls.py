from django.contrib import admin
from django.urls import path, include
from esender import views
urlpatterns = [
    path('',views.index,name='index')
    # path('',include('esender.urls')),
    # path('admin/', admin.site.urls),
]
