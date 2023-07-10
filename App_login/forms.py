from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from App_login.models import UserProfile

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Username','autofocus': 'True', 'class': 'form-control'}))
    email = forms.CharField(label='',widget=forms.EmailInput(attrs={'placeholder':'Email','class': 'form-control'}))
    password1 = forms.CharField( label='', widget=forms.PasswordInput(attrs={'placeholder':'Password','class': 'form-control'}))
    password2 = forms.CharField( label='', widget=forms.PasswordInput(attrs={'placeholder':'Confirm password','class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = UsernameField(label='', widget=forms.TextInput(attrs={'placeholder':'Username','autofocus': 'True', 'class': 'form-control'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password','autocomplete':'current-password','class': 'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Old Password','autofocus': 'True','autocomplete':'current-password','class': 'form-control'}))
    new_password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'New Password','autocomplete':'current-password','class': 'form-control'}))
    new_password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','autocomplete':'current-password','class': 'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class': 'form-control'}))

class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = UserProfile()
        exclude = ('user',)