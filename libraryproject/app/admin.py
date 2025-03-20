from django.contrib import admin
from .models import Book

# Register your models here.

class Bookadmin(admin.ModelAdmin):
    list_display=[
        "isbn",
        "title",
        "author",
        "category",
        "price",
        "qty",
        "dop",
        "description",
        "photo"
    ]
admin.site.register(Book, Bookadmin)