# forms.py

from django import forms
from .models import AnnouncedPuResult


class AnnouncedPuResultForm(forms.ModelForm):
    class Meta:
        model = AnnouncedPuResult
        fields = ['polling_unit', 'party', 'party_score']
