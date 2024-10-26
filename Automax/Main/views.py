from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Listing

def main_view(request):
    return render(request, 'main.html')

@login_required
def home_view(request):
    listings = Listing.objects.all()  # Fetch all listings

    context = {
        'listings': listings  # Passing listings directly
    }
    return render(request, 'home.html', context)

