from django import forms

from petstagram.pets.models import Pet


class PetCreateForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-field'

    class Meta:
        model = Pet
        exclude = ('user',)
