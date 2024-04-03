from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import CustomUser, Administrator,  Doctor


    
def homeView(request):
    return  render(request, "home.html", {})


def userCreateView(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        photo = request.POST.get("photo")
        country = request.POST.get("country")
        city = request.POST.get("city")
        uname = request.POST.get("username")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        state = request.POST.get("state")

        user = CustomUser.objects.create(uname, email,  password)
        user.first_name = fname
        user.last_name = lname
        user.country = country
        user.city = city
        user.state = state
        user.phone_number = phone
        user.photo = photo
        user.save()

        return redirect('login')
    return render(request, "registration/create_user.html", {})


def userLoginView(request):
    if request.method == "POST":
        name = request.POST.get('uname')
        password = request.POST.get('password')
        print(f"Username  : {name}")
        print(f"Password  : {password}")
        user = authenticate(request, username=name, password=password)

        if user is not None:
            
            login(request, user)
            return redirect('home')
        
        else:
            return HttpResponse("User not found!")
    return render(request, "login/user_login.html", {})



@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect("home")