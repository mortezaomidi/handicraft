from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LocationForm, ConstrainForm


def home(request):
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


def login(request):
    pass

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
    pass
