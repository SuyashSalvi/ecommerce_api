from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_user(request):
    if  request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('book-list')
        else:
            messages.error(request, 'Username or Password is incorrect.')
            # return redirect('login',{'error':'Username or Password Invalid'})
            # return redirect('/book-list')
    return render(request,'registration/login.html')
    # return redirect('/book-list')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    username = request.user
    return render(request, 'registration/profile.html',{'username':username})
