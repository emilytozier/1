"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя',min_length=2, max_length=100)
    city = forms.CharField(label='Город проживания', min_length=2, max_length=100)
    job = forms.CharField(label='Род занятий', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Ваш пол',
                             choices=[('1','Мужской'),('2','Женский')],
                             widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField ( label='Вы пользуетесь интернетом',
                                  choices=(('1','Каждый день'),
                                           ('2','Несколько раз в неделю'),
                                           ('3','Несколько раз в месяц'),
                                           ('4', 'Несколько раз в день')), initial=1)
    notice = forms.BooleanField (label='Получать новости сайта на e-mail?',
                           required=False)
    email= forms.EmailField(label='Ваш e-mail', min_length=7)
    message = forms.CharField(label='Коротко о себе',
                              widget=forms.Textarea(attrs={'rows':12,'cols':20}))