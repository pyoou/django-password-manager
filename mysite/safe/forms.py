from django import forms


class SafeForm(forms.Form):
    purpose = forms.CharField(max_length=300, label="", widget=forms.TextInput(attrs={'placeholder': 'purpose'}))
    content = forms.CharField(max_length=300, label="", widget=forms.PasswordInput(attrs={'placeholder': 'content'}))


class PasswordCheck(forms.Form):
    password = forms.CharField(max_length=300, label="", widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
