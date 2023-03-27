from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignupForm, BlogPostForm


def home(request):
    return HttpResponse("<h1>Accueil du site !</h1>")


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return "Merci de vous être inscrits au site"
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})




