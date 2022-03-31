from email.policy import default
from tokenize import blank_re
from unicodedata import category
from django.db import models
import uuid

# Create your models here.
class Gigs(models.Model):

    _id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, primary_key=True
    )

    nickname = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.CharField(max_length=12, default="no")

    title = models.CharField(max_length=25)

    category_options = (
        ("data analysis", "data analysis"),
        ("Advocacy & Awareness", "Advocacy & Awareness"),
        ("Music / Songwriting", "Music / Songwriting"),
        ("Shooting & Editing", "Shooting & Editing"),
        ("sales & marketing", "sales & marketing"),
        ("software development", "software development"),
        ("Recruiting & Test Prep", "Recruiting & Test Prep"),
        ("Other", "Other"),
    )
    category = models.CharField(max_length=200, choices=category_options)

    # image_1 = models.ImageField(null=True, blank=True)
    # image_2 = models.ImageField(null=True, blank=True)
    # image_3 = models.ImageField(null=True, blank=True)

    email = models.CharField(max_length=200)

    description = models.TextField(max_length=250)

    approval_options = (("yes", "yes"), ("no", "no"), ("pending", "pending"))

    approved = models.CharField(
        max_length=7, choices=approval_options, default="pending"
    )

    # @property
    # def image_2_url(self):
    #     if self.image_2 and hasattr(self.image_2, "url"):
    #         return self.image_2.url
    #     else:
    #         return "null"

    # @property
    # def image_3_url(self):
    #     if self.image_3 and hasattr(self.image_3, "url"):
    #         return self.image_3.url
    #     else:
    #         return "null"

    def __str__(self):
        return self.title


class contactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=300)
