from django.shortcuts import render

# Create your views here.
from app.common.profile import get_profile
from app.models import *
from app.views.profiles import create_profile


def index(request):
    if Profile.objects.exists():
        profile = get_profile()
        notes = Note.objects.all()

        context = {
            'profile': profile,
            'notes': notes
        }

        return render(request, 'home-with-profile.html', context)
    return create_profile(request)
