from django.shortcuts import render

from django.http import JsonResponse


from foodfinder.forms import SearchForm
from foodfinder.models import Food
from .models import Favor


# Create your views here.
def favors(request):

    form = SearchForm()

    favors = Favor.objects.filter(account=request.user).order_by('date').all()

    history = request.user.foodhistory_set.order_by('date').all()[:16]

    context = {
        'form': form,
        'favors': favors,
        'history': history,
    }

    return render(request, 'foodfinder/favors_page.html.django', context)

def add_favor(request, food_code, original_food_code):

    json = {'success': False}

    food = Food.objects.get(code=food_code)
    substitute_of = Food.objects.get(code=original_food_code)

    if food is not None:
        Favor.objects.create(account=request.user, food=food, substitute_of=substitute_of)
        json['success'] = True

    return JsonResponse(json)

def del_favor(request, favor_id):

    json = {'success': False}

    favor = Favor.objects.get(id=favor_id)

    if favor is not None:
        favor.delete()
        json['success'] = True

    return JsonResponse(json)
