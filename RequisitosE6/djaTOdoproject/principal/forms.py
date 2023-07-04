from django import forms
from django.contrib.auth.models import User

from django.utils import timezone
from datetime import datetime



from .models import Task



class UsuarioForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name', 'email',]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
        initial=datetime.now()
    )
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    status = forms.ChoiceField(
        choices=Task.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'label']

    def save(self, commit=True):
        task = super().save(commit=False)
        if commit:
            task.save()
        return task