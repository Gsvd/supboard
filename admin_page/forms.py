import datetime
from django import forms
from planning.models import Planning
from . import utils


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}), label="Username", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-input"}), label="Password", max_length=100)


class ClassroomForm(forms.Form):
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    if utils.grade_has_course(1):
        initial = Planning.objects.filter(date=today, grade=1)[0].classroom
        grade_1 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}), label="A.Sc.1", max_length=100, initial=initial, required=False)
    if utils.grade_has_course(2):
        initial = Planning.objects.filter(date=today, grade=2)[0].classroom
        grade_2 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}), label="A.Sc.2", max_length=100, initial=initial, required=False)
    if utils.grade_has_course(3):
        initial = Planning.objects.filter(date=today, grade=3)[0].classroom
        grade_3 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}), label="B.Sc", max_length=100, initial=initial, required=False)
    if utils.grade_has_course(4):
        initial = Planning.objects.filter(date=today, grade=4)[0].classroom
        grade_4 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}), label="M.Sc.1", max_length=100, initial=initial, required=False)
    if utils.grade_has_course(5):
        initial = Planning.objects.filter(date=today, grade=5)[0].classroom
        grade_5 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}), label="M.Sc.2", max_length=100, initial=initial, required=False)


class UploadForm(forms.Form):
    csvFile = forms.FileField(label="Course calendar")
