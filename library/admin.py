from django.contrib import admin
from .models import Category, Book


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
        "updated_at",
    )  
    search_fields = ("name",) 
    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )  


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "number_of_pages",
        "description",
        "category",
        "created_at",
        "updated_at"
    )
    list_filter = (
        "category",
        "author",
    ) 
    search_fields = ("title", "author", "description")
    readonly_fields = ("id", "created_at", "updated_at")
    raw_id_fields = ("category",)  


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
