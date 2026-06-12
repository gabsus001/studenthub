from django.urls import path
from .views import dashboard, subject_detail  # Dodaliśmy import subject_detail

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('subject/<int:subject_id>/', subject_detail, name='subject_detail'),  # Dynamiczny URL
]