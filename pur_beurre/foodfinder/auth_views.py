from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm
from .models import Account


# Create your views here.
def register_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid() :

            cd = form.cleaned_data

            try:
                account = Account()
                account.create_account_and_user(cd['name'], cd['email'], cd['password'])
                account.login_account(request)

                return redirect('home')
            except:
                print('error')

    context = {
        'form': form,
    }

    return render(request, 'auth/register.html.django', context)


def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid() :

            cd = form.cleaned_data

            account = Account.authenticate(cd['email'], cd['password'])

            if account:

                account.login_account(request)

                return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'auth/login.html.django', context)


def logout_view(request):

    logout(request)

    return redirect('login_view')
