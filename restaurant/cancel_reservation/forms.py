from django import forms
from .models import Reservation  # 正確的模型名稱是Reservation

class CancellationForm(forms.ModelForm):
    class Meta:
        model = Reservation  # 正確的模型名稱是Reservation
        fields = ['name', 'phone', 'date', 'time']
