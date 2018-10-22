from django import forms
from django.contrib.auth.models import User

from .models import Page, Category, UserProfile

class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=128, help_text='Informe a categoria')
    views = forms.IntegerField(label='Views', widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(label='Curtidas', widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(label='Título', max_length=128, help_text='Título da página')
    url = forms.URLField(label='URL', max_length=200, help_text='URL da página')
    views = forms.IntegerField(label='Views',widget=forms.HiddenInput, initial=0)

    class Meta:
        model = Page
        exclude = ('category',)

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')