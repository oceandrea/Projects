from django.shortcuts import render
from django.views.generic import TemplateView


# def landing_page(request):
#     context = {
#         'title': 'Petstagram',
#     }
#     return render(request, 'landing_page.html', context)


class HomeView(TemplateView):
    template_name = 'landing_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Petstagram'
        return context
