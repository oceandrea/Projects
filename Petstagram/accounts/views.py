import os

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import ProfileForm
from accounts.models import UserProfile
from pets.models import Pet


@login_required
def show_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(id=pk)
    own_profile = user == request.user
    if request.method == 'POST':
        old_photo = user.userprofile.profile_picture
        form = ProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            if request.FILES:
                os.remove(old_photo.path)
            form.save()
            redirect('user profile')

    context = {
        'own_profile': own_profile,
        'profile_user': user,
        'form': ProfileForm(),
        'pets': [pet for pet in Pet.objects.all() if pet.user.user == user],
    }
    return render(request, 'registration/profile.html', context)


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user,
            )
            profile.save()
            login(request, user)
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'registration/sign_up.html', context)
