import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import PetCreateForm
from petstagram.pets.models import Pet, Like


def pet_all(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets,
    }
    return render(request, 'pets/pet_list.html', context)


def show_pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    likes = [like.user.user for like in Like.objects.all() if like.pet == pet]
    comments = [comment for comment in Comment.objects.all() if comment.pet == pet]
    form = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(comment=form.cleaned_data['comment'], pet=pet, user=request.user.userprofile)
            comment.save()
            return redirect('pet details', pk)

    if not form:
        form = CommentForm()

    context = {
        'pet': pet,
        'likes': len(likes),
        'form': form,
        'comments': comments,
        'is_owner': pet.user.user == request.user,
        'can_like': request.user.is_authenticated and pet.user.user != request.user and request.user not in likes,
        'liked': pet.user.user != request.user and request.user in likes,
    }
    return render(request, 'pets/pet_detail.html', context)


@login_required
def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    user_liked = pet.like_set.filter(user_id=request.user.userprofile.id)
    if user_liked:
        user_liked.first().delete()
    else:
        like = Like(like=pet.name, user=request.user.userprofile)
        like.pet = pet
        like.save()
    return redirect('pet details', pk)


@login_required
def create_pet(request):
    form = None
    if request.method == 'POST':
        form = PetCreateForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user.userprofile
            pet.save()
            return redirect('all pets')
    if not form:
        form = PetCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'pets/pet_create.html', context)


@login_required
def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = None
    if request.method == 'POST':
        form = PetCreateForm(request.POST, request.FILES, instance=pet)
        old_image = pet.image
        new_image = 'image' in form.changed_data
        if form.is_valid():
            if new_image:
                os.remove(old_image.path)
            pet = form.save()
            pet.save()
            return redirect('all pets')

    if not form:
        form = PetCreateForm(instance=pet)

    context = {
        'form': form,
    }
    return render(request, 'pets/pet_edit.html', context)


@login_required
def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('all pets')

    context = {
        'pet': pet,
    }
    return render(request, 'pets/pet_delete.html', context)
