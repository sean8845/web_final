from django import forms
from .models import Cancellation

class CancellationForm(forms.ModelForm):
    class Meta:
        model = Cancellation
        fields = ['name', 'phone', 'date', 'time']
