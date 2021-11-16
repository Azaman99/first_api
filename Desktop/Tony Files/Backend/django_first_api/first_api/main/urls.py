from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students),
    path("students/<int:student_id>", views.student_detail),
    path('books/', views.books),
    path('books/<int:book_id>', views.book_detail),
    path('cohort/', views.cohort_list)
]