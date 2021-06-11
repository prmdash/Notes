from django.shortcuts import render, redirect

from app.common.profile import get_profile
from app.forms.profile import ProfileForm
from app.models import Note


def profile_index(request):
    profile = get_profile()
    notes_count = len(profile.note_set.all())

    context = {
        'profile': profile,
        'notes_count': notes_count
    }

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'GET':
        context = {
            'form': ProfileForm()
        }

        return render(request, 'home-no-profile.html', context)

    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'home-no-profile.html', context)
