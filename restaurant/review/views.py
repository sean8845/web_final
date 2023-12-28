# views.py
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


def write_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()

    return render(request, 'review/write_review.html', {'form': form})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review/review_list.html', {'reviews': reviews})

