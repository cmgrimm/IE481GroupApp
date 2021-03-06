"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from app.models import classSection
from django.utils.translation import ugettext_lazy as _
from app.classChoices import getChoices

class newclass(forms.Form):
    class1 = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Class'}))
    section = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Section'}))
    day = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Day'}))
    time1 = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Time'}))

class loginForm(forms.Form):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class NewAccount(forms.Form):
    firstName = forms.CharField(label='First Name',
                              max_length=30,
                              widget=forms.TextInput({
                                  'class': 'form-control',
                                  'placeholder': 'First Name'}))

    lastName = forms.CharField(label='Last Name',
                              max_length=30,
                              widget=forms.TextInput({
                                  'class': 'form-control',
                                  'placeholder': 'Last Name'}))

    username = forms.CharField(label='Username',
                              max_length=30,
                              widget=forms.TextInput({
                                  'class': 'form-control',
                                  'placeholder': 'username'}))

    email = forms.CharField(label='Email',
                              max_length=30,
                              widget=forms.EmailInput({
                                  'class': 'form-control',
                                  'placeholder': 'Email Address'}))

    birthday = forms.CharField(label='Birthday',
                              max_length=30,
                              widget=forms.DateInput({
                                  'class': 'form-control',
                                  'placeholder': 'MM/DD/YYYY'}))

    password1 = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

    password2 = forms.CharField(label=_("Confirm Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Confirm Password'}))

class Profilef(forms.Form):

    city = forms.CharField(label='City:',
                           max_length=30,
                           widget=forms.TextInput({
                             'class': 'form-control',
                             'placeholder': 'City'}))

    #photo = forms.FileField(label='Profile Photo:',
    #                       max_length=30,
    #                       widget=forms.FileInput({
    #                       'class': 'control-label'}))

    profileText = forms.CharField(label="Profile text:",
                                  max_length=1500,
                                  widget=forms.Textarea({
                                 'class': 'form-control',
                                 'placeholder': 'I M Kewl',
                                 'rows':'5'}))


    Level = (
    (0, _('Freshmen')),
    (1, _('Sophomore')),
    (2, _('Junior')),
    (3, _('Senior'))
    )

    grade = forms.ChoiceField(label = "Grade:", 
                                   choices=Level)

    mjr = (
    (0, _('Industrial Engineering')),
    (1, _('Mechanical Engineering')),
    (2, _('Design Engineering'))
    )

    major = forms.ChoiceField(label = "Major:", 
                                   choices=mjr)

class messageForm(forms.Form):
    receiver = forms.CharField(label=_("To:"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'username'}))
    subject = forms.CharField(label=_("Subject:"),max_length=100,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'Text'}))
    contents = forms.CharField(label=_("Body:"),max_length=2500,
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder':'Text'}))

class addClass(forms.Form): 
    addclass= forms.CharField(label="",required=True,
                                 widget = forms.Select({
                                     'choices':""
                                     })
                             )
