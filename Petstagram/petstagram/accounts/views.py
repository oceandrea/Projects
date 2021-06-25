import os

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from petstagram.accounts.forms import ProfileForm
from petstagram.accounts.models import UserProfile
from petstagram.pets.models import Pet


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/profile.html'
    form_class = ProfileForm
    model = UserProfile
    success_url = reverse_lazy('user profile')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        user = self.request.user if pk is None else User.objects.get(id=pk)

        return user.userprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = self.get_object().user
        context['own_profile'] = self.get_object().user == self.request.user
        context['pets'] = [pet for pet in Pet.objects.all() if pet.user.user == self.get_object().user]

        return context

    def dispatch(self, request, *args, **kwargs):
        old_picture = self.get_object().profile_picture
        if ('profile_picture' in request.FILES or 'profile_picture-clear' in request.POST) and old_picture:
            os.remove(old_picture.path)
        return super().dispatch(request, *args, **kwargs)


class RegisterView(CreateView):
    template_name = 'registration/sign_up.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        main_form = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return main_form
