from django.contrib.auth import login, authenticate, logout

from django.shortcuts import render, redirect

from .models import Account
from .forms import RegisterForm, LoginForm


# Create your views here.
def register_view(request):

    if request.user.is_authenticated:
        return redirect(request.GET.get('next', default='home'))

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid() :

            cd = form.cleaned_data

            if cd['password'] == cd['password_2']:

                try:
                    user = Account.objects.create_user(cd['name'], cd['email'], cd['password'])
                    login(request, user)

                    return redirect(request.GET.get('next', default='home'))
                except:
                    print('error')

    context = {
        'form': form,
    }

    return render(request, 'auth/register.html.django', context)


def login_view(request):

    if request.user.is_authenticated:
        return redirect(request.GET.get('next', default='home'))

    form = LoginForm()

    next = request.GET.get('next', default='home')

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid() :

            cd = form.cleaned_data

            user = Account.objects.filter(email=cd['email']).first()
            if user is not None:
                user = authenticate(username=user.username, password=cd['password'])
            else:
                user = authenticate(username=cd['email'], password=cd['password'])

            if user:
                login(request, user)
                return redirect(next)

    context = {
        'form': form,
        'next': next,
    }

    return render(request, 'auth/login.html.django', context)


def logout_view(request):

    logout(request)

    return redirect('login_view')
