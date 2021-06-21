from django.contrib import admin

from pets.models import Like, Pet


class LikeInline(admin.TabularInline):
    model = Like


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name')
    list_filter = ('type',)
    inlines = (
        LikeInline,
    )


admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
