from django.shortcuts import render


def landing_page(request):
    context = {
        'title': 'Petstagram',
    }
    return render(request, 'landing_page.html', context)
