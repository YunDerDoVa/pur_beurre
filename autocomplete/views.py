from django.shortcuts import render
from django.http import JsonResponse


from foodfinder.models import Food


# Create your views here.
def foodname(request):

    name = request.GET['name']

    dict = {'names': []}

    foods = Food.objects.filter(name__icontains=name).all()[:5]

    for food in foods:
        dict['names'].append(food.name)

    return JsonResponse(dict)
