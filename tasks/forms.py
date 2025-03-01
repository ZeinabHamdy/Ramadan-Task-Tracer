from django import forms
from .models import Task



class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'goal','current_achieved']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        #     'goal': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'current_achieved': forms.NumberInput(attrs={'class': 'form-control'}),
        # }