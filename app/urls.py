from django.urls import path

from app.views.index import index
from app.views.profiles import create_profile, profile_index

urlpatterns = (
    # Index
    path('', index, name='index'),


    # Profiles
    path('profile/', profile_index, name='view profile'),
    path('profile/create/', create_profile, name='create profile'),
)
