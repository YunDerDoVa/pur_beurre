from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


from foodfinder.forms import SearchForm
from foodfinder.models import Food
from .models import Favor


# Create your views here.
@login_required(login_url='/auth/login/')
def favors(request):

    form = SearchForm()

    favors = Favor.objects.filter(account=request.user).order_by('date').all()

    history = request.user.foodhistory_set.all()

    context = {
        'form': form,
        'favors': favors,
        'history': history,
    }

    return render(request, 'foodfinder/favors_page.html.django', context)


@login_required(login_url='/auth/login/')
def add_favor(request, food_code, original_food_code):

    json = {'success': False}

    food = Food.objects.get(code=food_code)
    substitute_of = Food.objects.get(code=original_food_code)

    if food is not None:
        Favor.objects.create(account=request.user, food=food, substitute_of=substitute_of)
        json['success'] = True

    return JsonResponse(json)


@login_required(login_url='/auth/login/')
def del_favor(request, favor_id):

    json = {'success': False}

    favor = Favor.objects.get(id=favor_id)

    if favor is not None:
        favor.delete()
        json['success'] = True

    return JsonResponse(json)
