from django.urls import path

from app.views.index import index
from app.views.profiles import create_profile

urlpatterns = (
    # Index
    path('', index, name='index'),


    # Profiles
    path('profile/create/', create_profile, name='create profile'),
)