from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import PetCreateForm
from petstagram.pets.models import Pet, Like


class AllPets(ListView):
    template_name = 'pets/pet_list.html'
    model = Pet
    context_object_name = 'pets'


class CommentCreate(LoginRequiredMixin, FormView):
    form_class = CommentForm
    model = Comment

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.pet_details = Pet.objects.get(pk=self.kwargs['pk'])
        comment.user = self.request.user.userprofile
        comment.save()
        return redirect('pet details', self.kwargs['pk'])


class PetDetails(DetailView):
    template_name = 'pets/pet_detail.html'
    model = Pet
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = self.get_object()
        context['form'] = CommentForm()

        likes = [like.user.user for like in pet.like_set.all()]
        context['likes'] = len(likes)

        context['comments'] = pet.comment_set.all()

        context['is_owner'] = pet.user.user == self.request.user
        context['can_like'] = self.request.user.is_authenticated and pet.user.user != self.request.user and self.request.user not in likes

        context['liked'] = pet.user.user != self.request.user and self.request.user in likes

        return context


class PetLike(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        pet = Pet.objects.get(pk=pk)
        user_liked = pet.like_set.filter(user_id=request.user.userprofile.id)
        if user_liked:
            user_liked.first().delete()
        else:
            like = Like(like=pet.name, user=request.user.userprofile)
            like.pet = pet
            like.save()
        return redirect('pet details', pk)


class CreatePet(LoginRequiredMixin, CreateView):
    template_name = 'pets/pet_create.html'
    form_class = PetCreateForm
    model = Pet
    success_url = reverse_lazy('all pets')

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user.userprofile
        pet.save()
        return super().form_valid(form)


class EditPet(LoginRequiredMixin, UpdateView):
    template_name = 'pets/pet_edit.html'
    form_class = PetCreateForm
    model = Pet
    success_url = reverse_lazy('all pets')


class DeletePet(LoginRequiredMixin, DeleteView):
    template_name = 'pets/pet_delete.html'
    model = Pet
    success_url = reverse_lazy('all pets')
