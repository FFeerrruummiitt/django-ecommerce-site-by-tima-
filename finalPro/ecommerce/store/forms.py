import re
from django.forms import ModelForm
# from .models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # add a custom validator to the password field
        self.fields['password1'].validators.append(
            self.validate_password_contains_number
        )

    def validate_password_contains_number(self, value):
        if not any(char.isdigit() for char in value):
            raise ValidationError('The password must contain at least one number.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError('Password must contain at least one uppercase letter.')
        return password



