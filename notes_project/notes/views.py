from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .forms import UserRegistrationForm, UserLoginForm, NoteForm
from .models import Note


def home_view(request):
    return render(request, "notes/base.html")


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "notes/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("note-list")
    else:
        form = UserLoginForm()
    return render(request, "notes/login.html", {"form": form})


@login_required
def note_list_view(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, "notes/note_list.html", {"notes": notes})


@login_required
def note_create_view(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("note-list")
    else:
        form = NoteForm()
    return render(
        request,
        "notes/note_form.html",
        {"form": form, "form_title": "Create Note", "button_text": "Create"},
    )


@login_required
def note_update_view(request, pk):
    note = Note.objects.get(pk=pk, user=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note-list")
    else:
        form = NoteForm(instance=note)
    return render(
        request,
        "notes/note_form.html",
        {"form": form, "form_title": "Edit Note", "button_text": "Update"},
    )


@login_required
def note_delete_view(request, pk):
    note = Note.objects.get(pk=pk, user=request.user)
    if request.method == "POST":
        note.delete()
        return redirect("note-list")
    return render(request, "notes/note_confirm_delete.html", {"note": note})
