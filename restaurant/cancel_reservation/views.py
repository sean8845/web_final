from django.shortcuts import render, redirect
from .forms import CancellationForm

def cancel_reservation(request):
    if request.method == 'POST':
        form = CancellationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cancel-success')
    else:
        form = CancellationForm()

    return render(request, 'cancel_reservation/cancel_reservation.html', {'form': form})

def cancel_success(request):
    return render(request, 'cancel_reservation/cancel_success.html')
