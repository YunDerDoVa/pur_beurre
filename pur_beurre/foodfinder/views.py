from django.shortcuts import render

# Create your views here.
def register(request):

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid() :
            form.handle_form()

            return redirect('home')

    context = {
        'form' = form,
    }

    return render(request, 'auth/register.html.django', context)
