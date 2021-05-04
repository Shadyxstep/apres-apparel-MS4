from django import forms
from .models import Athletes
from .widgets import CustomClearableFileInput


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athletes
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'sport': 'Sport',
            'background': 'Background',
            'image_url': 'Image Link',
            'social_url': 'Instagram Link',
            'social_url2': 'LinkedIn Link',
            'image': 'Image',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'input-shadow'
            self.fields[field].label = False