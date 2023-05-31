from .models import todo_task
from django import forms


class todo_form(forms.ModelForm):
    class Meta:
        model=todo_task
        fields=['name','priority','date']