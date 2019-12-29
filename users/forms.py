from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

BLOOD_GROUP_CHOICES = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    # blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES, label='Choose Blood Group',)
    # age = forms.CharField(max_length=100)
    # phone_number = forms.CharField(max_length=12)
    terms_and_conditions = forms.BooleanField(widget=forms.CheckboxInput, label='I have red and agree to the <a href="./terms_condition_privacy_policy.html" target="_blank">Terms and Conditions and Privacy Policy</a>' )
    # latitude = forms.FloatField()
    # longitude = forms.FloatField()
    # first_name = forms.CharField()
    # last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'terms_and_conditions']


class UserUpdateForm(forms.ModelForm):  # model form allows us to create a form  that works with specific database model
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['blood_group', 'age', 'phone_number', 'latitude', 'longitude', 'terms_and_conditions']

