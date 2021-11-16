from django.contrib import admin

from main.models import Student, Book

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "cohort", "date_joined"]
    list_per_page = 3
    list_filter = ["date_joined"]
    search_field = ("name", "cohort")

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "num_of_pages"]
    list_per_page = 3
    search_field = ("title", "author")