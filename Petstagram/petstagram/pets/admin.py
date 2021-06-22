from django.contrib import admin

from petstagram.common.models import Comment
from petstagram.pets.models import Like, Pet


class LikeInline(admin.TabularInline):
    model = Like


class CommentInline(admin.TabularInline):
    model = Comment


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name')
    list_filter = ('type',)
    inlines = (
        LikeInline,
        CommentInline,
    )


admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
