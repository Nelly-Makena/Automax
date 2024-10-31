from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Listing
from .forms import ListingForm
from Users.forms import LocationForm
from .filters import ListingFilter




def main_view(request):
    return render(request, 'main.html')


@login_required
def home_view(request):
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)

    context = {
        'listings': listing_filter.qs,  # Apply the filter to the queryset
        'listing_filter': listing_filter  # Pass the filter to use it in the template
    }

    return render(request, "home.html", context)


@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST, )
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(
                    request, f'{listing.model} Listing Posted Successfully!')
                return redirect('home')
            else:
                raise Exception()
        except Exception as e:
            print(e)
            messages.error(
                request, 'An error occured while posting the listing.')
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()
    return render(request, 'list.html', {'listing_form': listing_form, 'location_form': location_form, })

@login_required
def listing_view(request, id):
    try:
        listing = get_object_or_404(Listing, id=id)
        return render(request, 'listing.html', {'listing': listing})
    except Listing.DoesNotExist:
        messages.error(request, f'Invalid UID {id} was provided for listing.')
        return redirect('home')

