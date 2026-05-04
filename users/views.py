from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(
                request,
                user,
                backend='django.contrib.auth.backends.ModelBackend'
            )
            redirect('/jobs/')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    error = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(
                request,
                user,
                backend='django.contrib.auth.backends.ModelBackend'
            )
            return redirect('/jobs/')
        else:
            error = 'Invalid username or password'

    return render(request, 'users/login.html', {'error': error})


def logout_view(request):
    logout(request)
    redirect('/jobs/')


def profile_view(request):
    return render(request, 'users/profile.html')


def history_view(request):
    return render(request, 'users/history.html')