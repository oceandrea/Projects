import os

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from petstagram.accounts.forms import ProfileForm
from petstagram.accounts.models import UserProfile
from petstagram.pets.models import Pet


# @login_required
# def show_profile(request, pk=None):
#     user = request.user if pk is None else User.objects.get(id=pk)
#     own_profile = user == request.user
#     if request.method == 'POST':
#         old_photo = user.userprofile.profile_picture
#         form = ProfileForm(request.POST, request.FILES, instance=user.userprofile)
#         if form.is_valid():
#             if request.FILES:
#                 os.remove(old_photo.path)
#             form.save()
#             redirect('user profile')
#
#     context = {
#         'own_profile': own_profile,
#         'profile_user': user,
#         'form': ProfileForm(),
#         'pets': [pet for pet in Pet.objects.all() if pet.user.user == user],
#     }
#     return render(request, 'registration/profile.html', context)


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/profile.html'
    form_class = ProfileForm
    model = UserProfile
    # context_object_name = 'profile_user'
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


# def register(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             profile = UserProfile(
#                 user=user,
#             )
#             profile.save()
#             login(request, user)
#             return redirect('home')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'registration/sign_up.html', context)


class RegisterView(CreateView):
    template_name = 'registration/sign_up.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        main_form = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return main_form
