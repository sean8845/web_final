from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.http import JsonResponse


def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation-success')
        else:
            print(form.errors) 
    else:
        form = ReservationForm()

    return render(request, 'create_reservation/create_reservation.html', {'form': form})

def reservation_success(request):
    return render(request, 'create_reservation/reservation_success.html')
