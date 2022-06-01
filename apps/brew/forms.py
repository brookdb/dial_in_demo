from django import forms
from .import models
from apps.roast.models import Roast
from apps.users.models import CustomUser
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import gettext_lazy as _


class AddBrew(forms.ModelForm):

    roastDate = forms.DateField(widget = forms.SelectDateWidget)
    roastID = forms.ModelChoiceField(queryset=Roast.objects.all(), widget=forms.HiddenInput(attrs={'id': 'roast-object-id'}), required=False)
    class Meta:
        model = models.Brew
        fields = ['roastID', 'roastDate', 'brew_method','bestRecipieID',]

    def __init__(self, *args, **kwargs):
        super(AddBrew, self).__init__(*args, **kwargs)
        self.fields['bestRecipieID'].queryset = models.Recipie.objects.filter(brewID=self.instance.id)
        self.fields['bestRecipieID'].required = False
        self.fields['bestRecipieID'].widget = forms.HiddenInput()
        self.fields['roastDate'].label = 'Roast Date'
        self.fields['brew_method'].label = 'Brew Method'

class AddBrewRecipie(forms.ModelForm):

    flavor_score = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '-10', 'max': '10', 'id':'flavor-score-range'}), required=True)
    TSD_score = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '-10', 'max': '10', 'id':'TSD-score-range'}), required=True)
    class Meta:
        model = models.Recipie
        fields = ('dose', 'grind', 'output', 'flavor_score', 'TSD_score', 'comment',)

    def __init__(self, *args, **kwargs):
        super(AddBrewRecipie, self).__init__(*args, **kwargs)
        self.fields['dose'].label =  _('Dose (g)')
        self.fields['grind'].label = _('Grind')
        self.fields['output'].label = _('Output (g)')

        self.fields['flavor_score'].label = _('Flavor Score')
        #self.fields['flavor_score'].widget = form
        self.fields['TSD_score'].label = _('Total soluiable disolved (TSD)')

        self.fields['comment'].label = _('Comments')
        self.fields['comment'].widget = forms.Textarea(attrs={'rows':3})
