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


    city = forms.CharField(label='City',
                           max_length=30,
                           widget=forms.TextInput({
                             'class': 'form-control',
                             'placeholder': 'City'}))


    profileText = forms.CharField(label="Profile text",
                                  max_length=1500,
                                  widget=forms.Textarea({
                                 'class': 'form-control',
                                 'placeholder': 'I M Kewl',
                                 'rows':'5'}))

    month = forms.ChoiceField(choices=("IE","ME","DE"))