from django.contrib import admin
from .models import Gigs
from django.contrib.admin.options import ModelAdmin


# Register your models here.
class GigsAdmin(ModelAdmin):
    list_display = ["nickname", "title", "email", "created_at", "approved"]
    list_filter = ["created_at", "approved"]


admin.site.register(Gigs, GigsAdmin)
