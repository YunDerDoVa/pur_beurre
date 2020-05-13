from django.shortcuts import render


# Create your views here.
def home(request):

    context = {}

    return render(request, 'foodfinder/home.html.django', context)
