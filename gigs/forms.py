from turtle import textinput
from django.forms import CharField, ModelForm, Select, TextInput, Textarea
from .models import Gigs, Listing


class gigsForm(ModelForm):
    class Meta:
        model = Gigs
        fields = ["email", "category", "description", "title", "nickname"]
        widgets = {
            "title": TextInput(
                attrs={
                    "required": "True",
                    "class": "outline-none text-slate-700 bg-transparent w-auto",
                    "maxlength": 25,
                    "placeholder": "Junior Front End",
                }
            ),
            "nickname": TextInput(
                attrs={
                    "required": "True",
                    "class": "outline-none text-slate-700 bg-transparent w-auto",
                    "maxlength": 15,
                    "placeholder": "Mighty Jon",
                }
            ),
            "email": TextInput(
                attrs={
                    "required": "True",
                    "class": "outline-none text-slate-700 bg-transparent w-auto valid:bg-green-50 invalid:bg-red-50",
                    "maxlength": 35,
                    "placeholder": "as1036@duke.edu",
                    "id": "email--input",
                    "pattern": "^[A-Za-z0-9]+(@duke.edu)$",
                }
            ),
            "description": Textarea(
                attrs={
                    "rows": 6,
                    "class": "outline-none text-slate-700 bg-transparent w-full resize-none",
                    "maxlength": 250,
                    "placeholder": "I can create awesome websites with cool design using HTML and CSS. On top of that, I am awesome UX UI designer who uses figma Here is a link to my dribbble: xyz.com/zxc",
                }
            ),
        }


class listingsForm(ModelForm):
    class Meta:
        model = Listing
        fields = ["email", "category", "description", "title"]
        widgets = {
            "title": TextInput(
                attrs={
                    "required": "True",
                    "class": "outline-none text-slate-700 bg-transparent w-auto",
                    "maxlength": 25,
                    "placeholder": "Junior Front End",
                }
            ),
            "email": TextInput(
                attrs={
                    "required": "True",
                    "class": "outline-none text-slate-700 bg-transparent w-auto valid:bg-green-50 invalid:bg-red-50",
                    "maxlength": 35,
                    "placeholder": "as1036@duke.edu",
                    "id": "email--input",
                    "pattern": "^[A-Za-z0-9]+(@duke.edu)$",
                }
            ),
            "description": Textarea(
                attrs={
                    "rows": 8,
                    "class": "outline-none text-slate-700 bg-transparent w-full resize-none",
                    "maxlength": 450,
                    "placeholder": "I can create awesome websites with cool design using HTML and CSS. On top of that, I am awesome UX UI designer who uses figma Here is a link to my dribbble: xyz.com/zxc",
                }
            ),
        }
