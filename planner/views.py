from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Subject, Exam, Assignment, Note
from .forms import NoteForm, SubjectForm, ExamForm, AssignmentForm


@login_required
def dashboard(request):
    # 1. Pobieranie danych z bazy
    lista_przedmiotow = Subject.objects.filter(user=request.user)
    lista_egzaminow = Exam.objects.filter(subject__user=request.user).order_by('exam_date')
    lista_zadan = Assignment.objects.filter(subject__user=request.user).order_by('due_date')

    # 2. Domyślne tworzenie czystych formularzy dla żądania GET
    form_subject = SubjectForm()
    form_exam = ExamForm()
    form_assignment = AssignmentForm()

    # 3. Obsługa wysyłania formularzy (POST)
    if request.method == 'POST':
        if 'btn_subject' in request.POST:
            form_subject = SubjectForm(request.POST)
            if form_subject.is_valid():
                obj = form_subject.save(commit=False)
                obj.user = request.user
                obj.save()
                return redirect('dashboard')

        elif 'btn_exam' in request.POST:
            form_exam = ExamForm(request.POST)
            if form_exam.is_valid():
                form_exam.save()
                return redirect('dashboard')

        elif 'btn_assignment' in request.POST:
            form_assignment = AssignmentForm(request.POST)
            if form_assignment.is_valid():
                form_assignment.save()
                return redirect('dashboard')

    # 4. SŁOWNIK CONTEXT - SPRAWDŹ CZY MASZ TU WSZYSTKIE FORMULARZE!
    context = {
        'przedmioty': lista_przedmiotow,
        'egzaminy': lista_egzaminow,
        'zadania': lista_zadan,
        'form_subject': form_subject,  # To już działało
        'form_exam': form_exam,  # <-- SPRAWDŹ CZY TO MASZ
        'form_assignment': form_assignment,  # <-- SPRAWDŹ CZY TO MASZ
    }
    return render(request, 'planner/dashboard.html', context)


@login_required  # Szczegóły przedmiotu też blokujemy przed nieznajomymi
def subject_detail(request, subject_id):
    # Pobieramy przedmiot tylko, jeśli należy do zalogowanego użytkownika
    przedmiot = get_object_or_404(Subject, pk=subject_id, user=request.user)

    # Pobieramy notatki przypisane tylko do tego przedmiotu
    notatki = Note.objects.filter(subject=przedmiot).order_by('-created_at')

    # OBSŁUGA FORMULARZA:
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            notatka = form.save(commit=False)
            notatka.subject = przedmiot  # Automatycznie przypisujemy notatkę do tego przedmiotu
            notatka.save()
            return redirect('subject_detail', subject_id=przedmiot.id)  # Odświeżamy stronę po dodaniu
    else:
        form = NoteForm()  # Jeśli użytkownik po prostu wszedł na stronę, dajemy mu czysty formularz

    context = {
        'przedmiot': przedmiot,
        'notatki': notatki,
        'form': form,  # Przekazujemy zmienną 'form' do HTML-a
    }
    return render(request, 'planner/subject_detail.html', context)