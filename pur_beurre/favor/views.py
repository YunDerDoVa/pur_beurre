from django.shortcuts import render

from django.http import JsonResponse


from foodfinder.forms import SearchForm
from foodfinder.models import Food
from .models import Favor


# Create your views here.
def favors(request):

    form = SearchForm()

    favors = Favor.objets.filter(account=request.user).all()

    context = {
        'form': form,
        'favors': favors,
    }

    return render(request, 'foodfinder/favor_page.html.django', context)

def add_favor(request, food_code):

    json = {'success': False}

    food = Food.objects.get(code=food_code)

    if food is not None:
        Favor.objects.create(account=request.user, food=food)
        json['success'] = True

    return JsonResponse(json)
