from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name',
                  'date',
                  'class_name',
                  'class_letter',
                )
