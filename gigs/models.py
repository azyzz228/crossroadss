from unicodedata import category
from django.db import models
import uuid


class Categories(models.Model):
    category = models.CharField(max_length=200, unique=True, default="Other")

    def __str__(self):
        return self.category


class Gigs(models.Model):
    _id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, primary_key=True
    )
    nickname = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.CharField(max_length=12, default="no")
    title = models.CharField(max_length=25)
    category = models.ForeignKey(Categories, default=8, on_delete=models.SET_DEFAULT)
    email = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    approval_options = (("yes", "yes"), ("no", "no"), ("pending", "pending"))
    approved = models.CharField(
        max_length=7, choices=approval_options, default="pending"
    )
    # image_1 = models.ImageField(null=True, blank=True)
    # image_2 = models.ImageField(null=True, blank=True)
    # image_3 = models.ImageField(null=True, blank=True)
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


class Listing(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    deleted_options = (("yes", "yes"), ("no", "no"))
    is_deleted = models.CharField(max_length=12, default="no", choices=deleted_options)

    approval_options = (("yes", "yes"), ("no", "no"), ("pending", "pending"))
    approved = models.CharField(
        max_length=7, choices=approval_options, default="pending"
    )

    title = models.CharField(max_length=25)
    category = models.ForeignKey(Categories, default=8, on_delete=models.SET_DEFAULT)
    description = models.TextField(max_length=450)
    email = models.CharField(max_length=200)


class contactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=300)
