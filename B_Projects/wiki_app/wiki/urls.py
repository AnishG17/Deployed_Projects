from django.contrib import admin
from django.urls import path, include
from wiki import views
urlpatterns = [
    path('',views.index,name='index')
    # path('',include('wiki.urls')),
    # path('admin/', admin.site.urls),
]