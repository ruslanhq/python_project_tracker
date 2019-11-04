from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)
    first_name = forms.CharField(max_length=20, label='Name', required=False)
    last_name = forms.CharField(max_length=20, label='Last Name', required=False)

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('User with this email already exists', code='user_email_exists')
        except User.DoesNotExist:
            return email

    def clean(self):
        super().clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if not (first_name or last_name):
            raise ValidationError('Name or Last Name cannot be empty', code='name_or_last_name_empty')

        return self.cleaned_data


class UserUpdateForm(forms.ModelForm):
    avatar = forms.ImageField(label='Аватар', required=False)
    birth_date = forms.DateField(label='День рождения', input_formats=['%Y-%m-%d', '%d.%m.%Y'], required=False)
    about_me = forms.CharField(label='О себе', required=False, widget=forms.Textarea)
    git = forms.URLField(label='Профиль github', required=False)

    def get_initial_for_field(self, field, field_name):
        if field_name in self.Meta.profile_fields:
            return getattr(self.instance.profile, field_name)
        return super().get_initial_for_field(field, field_name)

    def save(self, commit=True):
        user = super().save(commit=commit)
        self.save_profile(commit)
        return user

    def save_profile(self, commit=True):
        profile, _ = Profile.objects.get_or_create(user=self.instance)
        for field in self.Meta.profile_fields:
            setattr(profile, field, self.cleaned_data.get(field))

        if not profile.avatar:
            profile.avatar = None

        if commit:
            profile.save()

    def clean_git(self):
        git = self.cleaned_data.get('git')


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar', 'birth_date', 'about_me', 'git']
        profile_fields = ['avatar', 'birth_date', 'about_me', 'git']


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
