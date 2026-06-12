from django import forms
from .models import Note, Subject, Exam, Assignment  # Sprawdź czy te cztery modele są zaimportowane!

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Wpisz treść nowej notatki...',
                'rows': 3
            }),
        }
        labels = {'content': ''}

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'lecturer']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'np. Algorytmy'}),
            'lecturer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'np. mgr Adam Bartosiewicz'}),
        }
        labels = {
            'name': 'Nazwa przedmiotu',
            'lecturer': 'Prowadzący',
        }

# Upewnij się, że ta nazwa to dokładnie ExamForm
class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['subject', 'title', 'exam_date']
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'np. Kolokwium'}),
            'exam_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

# Upewnij się, że ta nazwa to dokładnie AssignmentForm
class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['subject', 'title', 'due_date']
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'np. Projekt końcowy'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }