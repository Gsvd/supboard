import datetime
from django import forms
from supboard.enums import Grade


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}), label="Username", max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-input"}), label="Password", max_length=100, required=True)


class ClassroomForm(forms.Form):
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    grade_1 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}), label=Grade.ASC1.value, max_length=100, required=False)
    grade_2 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}), label=Grade.ASC2.value, max_length=100, required=False)
    grade_3 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}), label=Grade.BSC.value, max_length=100, required=False)
    grade_4 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}), label=Grade.MSC1.value, max_length=100, required=False)
    grade_5 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}), label=Grade.MSC2.value, max_length=100, required=False)


class UploadForm(forms.Form):
    csvFile = forms.FileField(label="Course calendar")
