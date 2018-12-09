from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LocationForm, ConstrainForm, SusForm


def login(request):
    if request.user.is_authenticated():
        return render(request, 'tourism/index.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('http://127.0.0.1:8000/')

        else:
            messages.error(request, 'نام کاربری یا گذرواژه اشتباه است')

    return render(request, 'tourism/login.html')


def home(request):
    if not request.user.is_authenticated():
        return redirect('http://127.0.0.1:8000/login')
    return render(request, 'tourism/index.html')


def babolsar(request):
    return render(request, 'tourism/babolsar.html')


def help(request):
    return render(request, 'tourism/help.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username,
                                     email=email,
                                     password=password,
                                     first_name=fname,
                                     last_name=lname)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(user)
            return render(request, 'tourism/location.html')
        else:
            return HttpResponse('آیا مطمئن هستید اطلاعات شما قبلا ثبت نشده است. آیا اطلاعات را به درستی وارد کرده اید ')
    else:
        return render(request, 'tourism/register.html')


def location(request):
    user = request.user
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.user = request.user
            location.save()
            return HttpResponse("اطلاعات با موفقیت ذخیره شد.")
    form = LocationForm()
    return render(request, 'tourism/location.html',{'form': form})

def constrain(request):
    user = request.user
    if request.method == 'POST':
        form = ConstrainForm(request.POST)
        if form.is_valid():
            constrain = form.save(commit=False)
            constrain.user = request.user
            constrain.save()
            return HttpResponse("اطلاعات با موفقیت ذخیره شد.")
    form = ConstrainForm()
    return render(request, 'tourism/location.html',{'form': form})

def best_location(request):
    pass


def sus(request):
    user = request.user
    if request.method == 'POST':
        form = SusForm(request.POST)
        if form.is_valid():
            criteria = form.save(commit=False)
            criteria.user = user
            criteria.save()
            return HttpResponse('با تشکر از مشارکت شما. نظرات شما با موفقیت ثبت شد.')
    else:
        form = SusForm()
    return render(request, 'tourism/sus.html', {'form': form})
