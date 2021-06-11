from django.shortcuts import render, redirect

from app.common.profile import get_profile
from app.forms.note import NoteForm, DeleteNoteForm
from app.models import Note


def create_note(request):
    if request.method == 'GET':
        context = {
            'form': NoteForm(),
        }

        return render(request, 'note-create.html', context)

    form = NoteForm(request.POST)
    if form.is_valid():
        note = form.save(commit=False)
        note.profile = get_profile()
        note.save()
        return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'note': note,
            'form': NoteForm(instance=note),
        }

        return render(request, 'note-edit.html', context)

    form = NoteForm(request.POST, instance=note)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'note': note,
        'form': form,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'note': note,
            'form': DeleteNoteForm(instance=note),
        }

        return render(request, 'note-delete.html', context)

    note.delete()
    return redirect('index')


def details_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'note': note,
            'form': NoteForm(instance=note),
        }

        return render(request, 'note-details.html', context)
