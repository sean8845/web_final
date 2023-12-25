# create_reservation/views.py

from django.shortcuts import render, redirect
from .forms import ReservationForm


def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # 表單驗證通過，處理表單並重定向    
            form.save()
            return redirect('reservation_success')
        else:
            # 表單驗證未通過，錯誤將被傳遞到模板
            print(form.errors)  # 可以在控制台中看到錯誤信息
    else:
        form = ReservationForm()

    # 返回帶有表單物件的頁面，這樣模板就可以訪問表單和錯誤信息
    return render(request, 'create_reservation/create_reservation.html', {'form': form})

def reservation_success(request):
    # 處理預定成功頁面的邏輯
    return render(request, 'create_reservation/reservation_success.html')
