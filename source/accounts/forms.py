from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username', required=True)
    password = forms.CharField(max_length=100, label='Password', required=True,
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, label='Password Confirm', required=True,
                                       widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', required=True)
    first_name = forms.CharField(max_length=20, label='Name', required=False)
    last_name = forms.CharField(max_length=20, label='Last Name', required=False)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('User with this email already exists', code='user_email_exists')
        except User.DoesNotExist:
            return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('User with this username already exists',
                                  code='username_exists')
        except User.DoesNotExist:
            return username

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data['password']
        password_2 = self.cleaned_data['password_confirm']
        if password_1 != password_2:
            raise ValidationError('Passwords do not match',
                                  code='passwords_do_not_match')

        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if not (first_name or last_name):
            raise ValidationError('Name or Last Name cannot be empty', code='name_or_last_name_empty')

        return self.cleaned_data


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class PasswordChangeForm(forms.ModelForm):
    old_password = forms.CharField(max_length=100, label='Old Password', required=True,
                               widget=forms.PasswordInput)
    password = forms.CharField(max_length=100, label='New Password', required=True,
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, label='New Password Confirm', required=True,
                                       widget=forms.PasswordInput)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user = self.instance
        if not user.check_password(old_password):
            raise ValidationError('Invalid password', code='invalid_password')
        return old_password

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data['password']
        password_2 = self.cleaned_data['password_confirm']
        if password_1 != password_2:
            raise ValidationError('Passwords do not match',
                                  code='passwords_do_not_match')
        return self.cleaned_data

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['old_password', 'password', 'password_confirm']
