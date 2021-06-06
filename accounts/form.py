from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction

from .models import User, UserAccount


class CustomerSignUpForm(UserCreationForm):

    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            # 'class': 'form-control',
            # 'placeholder': 'Full Name',
        }
    ))

    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            # 'class': 'form-control',
            # 'placeholder': 'Email',
        }
    ))

    phone_number = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            # 'class': 'form-control',
            # 'placeholder': 'Email',
        }
    ))

    password1 = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            # 'class': 'form-control',
            # 'placeholder': 'Password',
            'type': 'password',
        }
    ))

    password2 = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            # 'class': 'form-control',
            # 'placeholder': 'Confirm Password',
            'type': 'password',
        }
    ))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'phone_number', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.username = self.cleaned_data.get('username')
        user.save()
        customer = UserAccount.objects.create(user=user)
        customer.email = self.cleaned_data.get('email')
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.save()
        return user

