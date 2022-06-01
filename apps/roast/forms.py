from django import forms
from .import models

class AddRoast(forms.ModelForm):
    class Meta:
        model = models.Roast
        fields = ['name', 'region', 'variatal', 'process', 'producer', 'notes', 'thumb']

    def __init__(self, *args, **kwargs):
        super(AddRoast, self).__init__(*args, **kwargs)
        self.fields['thumb'].label = "Upload Thumbnail"
