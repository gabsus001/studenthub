from django.urls import path
# Dopisałem delete_exam oraz delete_assignment do importu na górze:
from .views import dashboard, subject_detail, delete_exam, delete_assignment

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('subject/<int:subject_id>/', subject_detail, name='subject_detail'),

    # Tutaj usuwamy "views.", zostawiamy same nazwy funkcji:
    path('exam/delete/<int:exam_id>/', delete_exam, name='delete_exam'),
    path('assignment/delete/<int:assignment_id>/', delete_assignment, name='delete_assignment'),
]