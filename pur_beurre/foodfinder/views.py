from django.shortcuts import render, redirect
from django.http import Http404


from .forms import SearchForm
from .models import Food
from .algorythms import Algorythm


# Create your views here.
def home(request):

    form = SearchForm()

    context = {
        'form': form,
    }

    return render(request, 'foodfinder/home.html.django', context)

def search(request):

    if request.method == 'POST':

        form = SearchForm(request.POST)

        search_term = form.get_search_term()

        algorythm = Algorythm.get_algorythm_by_classname('ByCategory')

        food = Food.get_food_by_search_term(search_term)

        if food is None:
            return redirect('home')

        substitutes = algorythm.search_substitutes(food, request.user)

    else:

        form = SearchForm()


    context = {
        'form': form,
        'food': food,
        'substitutes': substitutes,
    }

    # results : 2x3
    return render(request, 'foodfinder/results_page.html.django', context)

def food_page(request, code):

    form = SearchForm()

    food = Food.objects.get(code=code)

    context = {
        'form': form,
        'food': food,
    }

    return render(request, 'foodfinder/food_page.html.django', context)

def account_page(request):

    context = {
        'account': request.user,
    }

    return render(request, 'foodfinder/account_page.html.django', context)
