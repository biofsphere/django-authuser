from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_user
from django.contrib.auth import login as login_user

from .forms import SignUpForm
from .models import User


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                email=form.cleaned_data['email'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            login_user(request, user)
            return redirect('/')

    return render(request, 'registration/signup.html', {
        'form': form,
    })


def logout(request):
    logout_user(request)
    return redirect('/')