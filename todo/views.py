from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, reverse, get_list_or_404, get_object_or_404
from django.http import request
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Accounts, Goals
# Create your views here.


def home(request):
    if not request.user.is_authenticated:
        return render(request, 'dolist/login.html', {"message": None})

    x=request.user.username
    account = get_object_or_404(Accounts, user=x)
    goals= account.goals_set.all()
    return render(request, 'dolist/home.html', {'lists':goals})


def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'dolist/login.html', {'messages': 'not valid'})

def log_out(request):
    logout(request)
    return render(request, 'dolist/login.html', {'message': 'logged out'})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST['username']
        raw_password1 = request.POST['password1']
        raw_password2 = request.POST['password2']

        if len(raw_password1) < 8:
            form = UserCreationForm()
            return render(request, 'dolist/register.html', {'form': form, 'message': 'too short password'})

        if raw_password1 != raw_password2:
            form = UserCreationForm()
            return render(request, 'dolist/register.html', {'form': form, 'message': 'passwords not equal'})

        if form.is_valid():
            form.save()
            account = Accounts.objects.create(user=username)
            account.save()
            print(Accounts.objects.all())
            return redirect('home')
            
        form = UserCreationForm()
        return render(request, 'dolist/register.html', {'message': 'not Create Account', 'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'dolist/register.html', {'message': 'Create Account', 'form': form})



def add(request):
    todo = request.POST['todo']
    user = Accounts.objects.get(user=request.user.username)
    toadd = Goals.objects.create(accounts=user, goal=todo)
    toadd.save()
    return HttpResponseRedirect(reverse('home'))

def delete(request, id):
    Goals.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('home'))

def change(requset):
    x = requset.user.username
    account = get_object_or_404(Accounts, user=x)
    goals = account.goals_set.all()
    goals= list(goals)
    for item in goals:
        i = item.id 
        req = requset.POST[str(i)]
        if req:
            machines = machines.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('home'))
