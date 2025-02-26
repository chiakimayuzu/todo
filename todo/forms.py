from django import forms
from .models import Task

class RegistForm(forms.ModelForm):
    title = forms.CharField(label='タスク名')
    description = forms.CharField(label='詳細説明') 
    expiry = forms.DateField(
    label='期限',widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'YYYY-MM-DD'}))

    class Meta:
        model = Task
        fields = ['title','description','expiry']

class UpdateForm(forms.ModelForm):
    title = forms.CharField(label='タスク名')
    description = forms.CharField(label='詳細説明')
    expiry = forms.DateField(
    label='期限',widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'YYYY-MM-DD'}))

    class Meta:
        model = Task
        fields = ['title','description','expiry']


    