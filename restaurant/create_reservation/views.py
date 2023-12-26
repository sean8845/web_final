from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.http import JsonResponse
from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError


def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            # 在預訂創建成功後，將預訂的名稱存儲在會話中
            request.session['created_reservation_name'] = reservation.name
            return redirect('reservation-success')
        else:
            print(form.errors) 
    else:
        form = ReservationForm()

    return render(request, 'create_reservation/create_reservation.html', {'form': form})

def reservation_success(request):
    # 檢查會話中是否存在已創建的預訂名稱
    created_reservation_name = request.session.get('created_reservation_name')
    if created_reservation_name:
        # 如果存在，則顯示成功頁面
        del request.session['created_reservation_name']  # 清除會話中的名稱
        return render(request, 'create_reservation/reservation_success.html', {'created_reservation_name': created_reservation_name})
    else:
        # 如果不存在，可能是直接訪問了成功頁面，您可以根據需求處理
        return redirect('create-reservation')


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
            raise ValidationError('該日期、時間和桌次已經被預訂，請選擇其他時間或桌次。')

