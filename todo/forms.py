from django import forms
from .models import Todo

class TodoAddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'complated',)
        # exclude = ('created_date',)

class TodoDeleteForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'complated',)