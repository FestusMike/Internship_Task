from django.db import models
from utils.models import BaseModel

# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=255, null=False, unique=True)

    class Meta:
        abstract = False
        verbose_name_plural = "Categories"

class Book(BaseModel):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    number_of_pages = models.IntegerField(null=False)
    description = models.CharField(max_length=255, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="books")

    class Meta:
        abstract = False