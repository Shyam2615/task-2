from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):

    return render(request, 'homePage.html')

def register(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        user_type = request.GET.get('user')
        profile = request.FILES.get('profile')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirmpassword')
        address_line1 = data.get('address')
        city = data.get('city')
        state = data.get('state')
        zip_code = data.get('zip')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "User already exists")
            return redirect(f'/register/?user={user_type}')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect(f'/register/?user={user_type}')

        
        try:
            user = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                user_type = user_type,
                profile_picture = profile,
                address_line1 = address_line1,
                city = city,
                state = state,
                pincode = zip_code
            )
            user.set_password(password)
            user.save()

            if user_type == "doctor":
                doctor = Doctor.objects.create(user = user)
                doctor.user.save()
            else:
                patient = Patient.objects.create(user = user)
                patient.user.save()

            messages.info(request, "Account created successfully")
            login(request, user)
            return redirect(f'/dashboard/?user={user_type}')
        
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect(f'/register/?user={user_type}')

    user_type = request.GET.get('user')
    context = {'user_type': user_type}
    return render(request, 'register.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.GET.get('user')

        if not User.objects.filter(username = username).exists():
           messages.info(request, "Enter the correct username")
           return redirect(f'/login/?user={user_type}')
       
        user = authenticate(username=username, password=password)

        if user is None:
           messages.info(request, "Enter the correct password")
           return redirect(f'/login/?user={user_type}')
        else:
           login(request, user)
           return redirect(f'/dashboard/?user={user_type}')

    user_type = request.GET.get('user')
    context = {'user_type': user_type}
    return render(request, 'login.html', context)

@login_required(login_url='/')
def dashboard(request):
    user = request.user

    if user.user_type == "doctor":
        doctor = Doctor.objects.get(user=user)
        context = {
            'first_name': doctor.user.first_name,
            'last_name': doctor.user.last_name,
            'email': doctor.user.email,
            'profile_picture': doctor.user.profile_picture.url if doctor.user.profile_picture else None,
            'address_line1': doctor.user.address_line1,
            'city': doctor.user.city,
            'state': doctor.user.state,
            'pincode': doctor.user.pincode,
            'user_type' : doctor.user.user_type
        }
    else:
        patient = Patient.objects.get(user=user)
        context = {
            'first_name': patient.user.first_name,
            'last_name': patient.user.last_name,
            'email': patient.user.email,
            'profile_picture': patient.user.profile_picture.url if patient.user.profile_picture else None,
            'address_line1': patient.user.address_line1,
            'city': patient.user.city,
            'state': patient.user.state,
            'pincode': patient.user.pincode,
            'user_type' : patient.user.user_type
        }

    return render(request, 'dashboard.html', context)