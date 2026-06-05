from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(
             request,
             user,
             backend="django.contrib.auth.backends.ModelBackend"
)

            return redirect("/jobs/")

    else:

        form = RegisterForm()

    return render(
        request,
        "users/register.html",
        {
            "form": form
        }
    )


def login_view(request):

    error = ""

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect("/jobs/")

        error = "Invalid username or password"

    return render(
        request,
        "users/login.html",
        {
            "error": error
        }
    )


def logout_view(request):

    logout(request)

    return redirect("/login/")


@login_required
def profile_view(request):

    return render(
        request,
        "users/profile.html"
    )


@login_required
def history_view(request):

    return render(
        request,
        "users/history.html"
    )