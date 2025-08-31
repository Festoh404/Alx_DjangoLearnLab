from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ("title", "author", "publication_year")

    # Add filters in the sidebar
    list_filter = ("publication_year",)

    # Enable search functionality
    search_fields = ("title", "author")

# Register the model with its custom admin
admin.site.register(Book, BookAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "date_of_birth", "is_staff", "is_active"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
