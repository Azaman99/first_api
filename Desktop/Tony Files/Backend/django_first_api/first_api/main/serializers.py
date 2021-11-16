from django.db.models import fields
from rest_framework import serializers
from .models import Student, Book


class StudentSerializer(serializers.ModelSerializer):
    book = serializers.ReadOnlyField()

    class Meta:
        model = Student
        fields = ["name", "cohort", "date_joined", "book"]

class BookSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField()

    class Meta:
        model = Book
        fields = ["title", "author", "student", "student_name", "num_of_pages"]