from django.contrib import admin
from .models import Book,Author,Address,Country

# Register your models here.

admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "rating", "is_bestSelling")
    search_fields = ("title",)
    list_filter = ("is_bestSelling",)

admin.site.register(Address)
admin.site.register(Country)

admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")
    
    