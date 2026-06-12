from django.db import models
from django.contrib.auth.models import User  # Prawidłowo zaimportowany User


class Subject(models.Model):
    # Powiązanie z użytkownikiem na samym początku klasy
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subjects',
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100)
    lecturer = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Exam(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    exam_date = models.DateField()

    def __str__(self):
        return self.title


class Assignment(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Note(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title