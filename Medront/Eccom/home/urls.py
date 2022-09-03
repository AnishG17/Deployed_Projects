from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('',views.customer_signup,name='customer_signup'),
    path('',views.customer_login,name='customer_login'),
]