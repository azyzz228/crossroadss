from unicodedata import category
from django.shortcuts import render
from .forms import gigsForm
from .models import Gigs
from .filters import GigsFilter

# Create your views here.
def home(request):
    # list_of_gigs = Gigs.objects.filter(approved="yes")
    # if list_of_gigs.exists():
    #     context = {"gigs": list_of_gigs}
    # else:
    #     context = {"gigs": ""}

    return render(request, "gigs/HomepageV2.html")


def formPage(request):
    context = {"form": gigsForm}
    if request.method == "POST":
        newGig = Gigs()
        # GET values from the from
        nickname = request.POST.get("nickname")
        email = request.POST.get("email")
        title = request.POST.get("title")
        description = request.POST.get("description")
        category = request.POST.get("category")
        # Create new object and push it
        newGig.nickname = nickname
        newGig.email = email
        newGig.title = title
        newGig.description = description
        newGig.category = category
        newGig.save()
        return render(request, "gigs/Success.html")

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
