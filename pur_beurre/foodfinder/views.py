from django.shortcuts import render


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

        algorythm = Algorythm.get_algorythm_by_classname('ByFat')

        food = Food.objects.filter(name=search_term).first()

        substitutes = algorythm.search_substitutes(food)

    else:

        form = SearchForm()


    context = {
        'form': form,
        'food': food,
        'substitutes': substitutes,
    }

    # results : 2x3
    return render(request, 'foodfinder/results_page.html.django', context)
