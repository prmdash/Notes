from django import forms

from app.forms.common import DisabledFormMixin
from app.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ('profile',)


class DeleteNoteForm(NoteForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
