from django.forms import ModelForm
from .models import Gigs


class gigsForm(ModelForm):
    class Meta:
        model = Gigs
        fields = "__all__"
