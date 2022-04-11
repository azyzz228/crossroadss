from unicodedata import category
from django.shortcuts import render
from .forms import gigsForm, listingsForm
from .models import Categories, Gigs, Listing
from .filters import GigsFilter, ListingsFilter

# Create your views here.
def home(request):
    # list_of_gigs = Gigs.objects.filter(approved="yes")
    # if list_of_gigs.exists():
    #     context = {"gigs": list_of_gigs}
    # else:
    #     context = {"gigs": ""}

    return render(request, "gigs/HomepageV2.html")


def formPage(request):
    form = gigsForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print(request.POST)
            print(form)
            form.save()
            return render(request, "gigs/Success.html")
    context = {"form": form}

    return render(request, "gigs/Form.html", context)


def success(request):
    return render(request, "gigs/success.html")


def gigsPage(request):
    list_of_gigs = Gigs.objects.filter(approved="yes")
    myFilter = GigsFilter(request.GET, queryset=list_of_gigs)
    list_of_gigs = myFilter.qs

    if list_of_gigs.exists():
        context = {"gigs": list_of_gigs, "myFilter": myFilter}
    else:
        context = {"gigs": "nodata", "myFilter": myFilter}

    return render(request, "gigs/gigsPage.html", context)


def listingsPage(request):
    list_of_listings = Listing.objects.filter(approved="yes", is_deleted="no")
    myFilter = ListingsFilter(request.GET, queryset=list_of_listings)
    list_of_listings = myFilter.qs

    if list_of_listings.exists():
        context = {"listings": list_of_listings, "myFilter": myFilter}
    else:
        context = {"listings": "nodata", "myFilter": myFilter}

    return render(request, "gigs/listings.html", context)


def ListingForm(request):
    form = listingsForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print(request.POST)
            print(form)
            form.save()
            return render(request, "gigs/Success.html")
    context = {"form": form}
    return render(request, "gigs/ListingForm.html", context)


def test(request):
    form = listingsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {"form": form}

    return render(request, "gigs/test.html", context)
