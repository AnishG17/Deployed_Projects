from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):                     # Display all phones with all the fields.
    phone = Phone.objects.all()
    return render(request, "index.html", {'phone':phone})

def customer_signup(request):           # Sign up function for customer
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']   # Two passwords of security
        password2 = request.POST['password2']
        contact = request.POST['contact']       # contact number of customer
 
        if password1 != password2:
            return redirect("/customer_signup")
 
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
        user.save()          # the user model is used for creating user and info is saved in the Customer model after saving the user.
        customer = Customer(user=user, phone=contact,email=email, type="Customer")
        customer.save()
        alert = True         # after saving user will be directed to
        return render(request, "customer_signup.html", {'alert':alert})
    return render(request, "customer_signup.html") 

def customer_login(request): # Customer logging in function
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                user1 = Customer.objects.get(user=user)
                if user1.type == "Customer":
                    login(request, user)
                    return redirect("/customer_homepage")
            else:
                alert = True
                return render(request, "customer_login.html", {'alert':alert})
    return render(request, "customer_login.html")


def signOut(request):       # signout/logout function
    logout(request)
    return redirect('/')