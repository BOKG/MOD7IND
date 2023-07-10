from django import forms
from django.contrib.auth.models import User
import datetime


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
    user = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=User.objects.all(),
        # tomar al usuario que le pertenece la tarea
        initial=User.objects.first()
    )
    due_date = forms.DateField(
        widget=forms.DateInput(
            format='%d-%m-%Y',
            attrs={'class': 'form-control',
                   'type': 'date'
                   }
        ),
        initial=datetime.timedelta(days=30) + datetime.date.today()
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
        fields = ['user', 'title', 'description',
                  'due_date', 'status', 'label', 'priority']

    def save(self, commit=True):
        task = super().save(commit=False)
        if commit:
            task.save()
        return task
