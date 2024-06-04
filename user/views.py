from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from post.models import Post
from django.contrib import admin  
from .models import CustomUser, Administrator,  Doctor
from .forms import EditCustomUser

    
def homeView(request):
    posts = Post.objects.all()
    context = dict()
    context['posts'] = posts
    return  render(request, "home.html", context=context)

def doctorHomeView(request):
    context = {}
    return render(request, "home.html",  context=context)



def userLoginView(request):
    if request.method == "POST":
        name = request.POST.get('uname')
        password = request.POST.get('password')
        print(f"Username  : {name}")
        print(f"Password  : {password}")
        user = authenticate(request, username=name, password=password)

        if user is not None:
            if user.is_doctor==True and user.is_active == True:
                login(request, user)
                return redirect('home')
            
            elif user.is_active == True:
                login(request, user)
                return redirect("home")
            
            else:
                return  HttpResponse("User is disabled")
        
        else:
            return HttpResponse("User not found!")
    return render(request, "login/login.html", {})



@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect("home")



def userCreateView(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        country = request.POST.get("country")
        city = request.POST.get("city")
        uname = request.POST.get("username")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        state = request.POST.get("state")

        user = CustomUser.objects.create_user(uname, email,  password)
        user.first_name = fname
        user.last_name = lname
        user.country = country
        user.city = city
        user.state = state
        user.phone_number = phone
        user.save()

        return redirect('login')
    return render(request, "registration/create_user.html", {})





def createDoctor(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        country = request.POST.get("country")
        city = request.POST.get("city")
        uname = request.POST.get("username")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        state = request.POST.get("state")
        specialist = request.POST.get('specialist')
        user = CustomUser.objects.create_user(uname, email,  password)
        user.first_name = fname
        user.last_name = lname
        user.country = country
        user.city = city
        user.state = state
        user.phone_number = phone
        user.is_doctor = True
        user.save()

        doctor = Doctor.objects.create(user=user)
        doctor.specialist = specialist

        doctor.save()


        return redirect('login')

    return render(request, "registration/create_doctor.html", {})



@login_required(login_url='login')
def userProfile(request, uname):
    context = {}
    user = CustomUser.objects.get(username=uname)
    context["myuser"] = user
    
    if user.is_superuser and user.is_active :
        return render (request, "profiles/admin_profile.html", context=context) 
    elif user.is_doctor  and user.is_active:
        doctor = Doctor.objects.get(user=user)
        context["doctor"] = doctor
        return render (request, "profiles/doctor_profile.html", context=context)        
    elif user.is_active :
        return render(request, "profiles/user_profile.html", context=context)