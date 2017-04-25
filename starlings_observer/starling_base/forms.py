from django import forms

from .models import Death

class Death(forms.Death):

    class Meta:
        model = Death
        fields = ('Prep', 'Trap', 'Depredation_method')