from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if request.method == "POST":
        user = request.POST["user"]
        password = request.POST["Password"]
        email = request.POST["emailid"]
        user = User.objects.create_user(
            username = user,
            password = password,
            email = email
        )
        login(request,user)
        subject = 'welcome to GFG world'
        message = f'Hi {user.username1}, thank you for registering in geeksforgeeks.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email1, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect("/dashboard")
    return render(request,'index.html')