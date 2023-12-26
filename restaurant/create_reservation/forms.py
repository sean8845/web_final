from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'date', 'time', 'table']

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        table = cleaned_data.get('table')

        # 檢查是否存在相同的預訂
        existing_reservation = Reservation.objects.filter(date=date, time=time, table=table).first()
        if existing_reservation:
            raise ValidationError('該日期、時間和桌次已經被預訂，請選擇其他時間或桌次。', code='duplicate_reservation')
