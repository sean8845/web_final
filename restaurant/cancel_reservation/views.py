from django.shortcuts import render, redirect
from .forms import CancellationForm
from create_reservation.models import Reservation

from django.shortcuts import render, redirect
from .forms import CancellationForm
from create_reservation.models import Reservation
from django.core.exceptions import ValidationError

def cancel_reservation(request):
    error_message = None  # 初始化 error_message
    if request.method == 'POST':
        form = CancellationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            try:
                # 使用 Reservation 模型來查找預訂
                reservation = Reservation.objects.get(name=name, date=date, time=time)
                reservation.delete()
                return redirect('cancel-success')
            except Reservation.DoesNotExist:
                error_message = '查無此資料'
                print(f"No matching reservation found for {name} on {date} at {time}.")
                
        else:
            print(form.errors)
    else:
        form = CancellationForm()

    return render(request, 'cancel_reservation/cancel_reservation.html', {'form': form, 'error_message': error_message})

def cancel_success(request):
    # 此视图用于显示预订取消成功的页面
    return render(request, 'cancel_reservation/cancel_success.html')
