from django.urls import path

from app.views.index import index
from app.views.notes import create_note, edit_note, delete_note, details_note
from app.views.profiles import create_profile, profile_index

urlpatterns = (
    # Index
    path('', index, name='index'),

    # Notes
    path('notes/create/', create_note, name='create note'),
    path('notes/edit/<int:pk>/', edit_note, name='edit note'),
    path('notes/delete/<int:pk>/', delete_note, name='delete note'),
    path('notes/details/<int:pk>/', details_note, name='details note'),

    # Profiles
    path('profile/', profile_index, name='view profile'),
    path('profile/create/', create_profile, name='create profile'),
)
