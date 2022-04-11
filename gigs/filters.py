import django_filters
from django_filters.filters import (
    CharFilter,
)

from .models import *


class GigsFilter(django_filters.FilterSet):
    # platform = ChoiceFilter(choices="PLATFORM")
    # platform = CharFilter(field_name="platform")
    keywords = CharFilter(
        field_name="description",
        lookup_expr="icontains",
    )

    class Meta:
        model = Gigs
        fields = ["description", "category"]


class ListingsFilter(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = ["category"]
