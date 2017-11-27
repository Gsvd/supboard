from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}), label="Username", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-input"}), label="Password", max_length=100)


class UploadForm(forms.Form):
    csvFile = forms.FileField(label="Course calendar")
