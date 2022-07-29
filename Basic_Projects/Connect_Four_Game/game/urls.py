from django.contrib import admin
from django.urls import include, path
from game import views

urlpatterns = [
    # path('',inlcude('game.urls'))
    path('',views.index,name='index')
    # path('admin/', admin.site.urls),
    ]
