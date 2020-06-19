from django.shortcuts import render


# Create your views here.
def home(request):

    context = {}

    return render(request, 'foodfinder/home.html.django', context)

def search(request):

    context = {}

    # results : 2x3
    return render(request, 'foodfinder/results_page.html.django', context)
