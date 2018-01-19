import os
import errno
import time
import csv
import dateparser
import datetime
import pandas as pd

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from planning.models import Planning
from .forms import LoginForm, UploadForm, ClassroomForm
from supboard.enums import Url
from supboard.enums import RowTarget
from admin_page.utils import get_grade_by_id


def admin_index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(Url.ADMIN.value)
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = request.POST["username"]
                password = request.POST["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Authentication successful")
                    return HttpResponseRedirect(Url.ADMIN_PLANNING_UPLOAD.value)
                else:
                    messages.error(request, "User incorrect")
                    return HttpResponseRedirect(Url.ADMIN.value)
        else:
            form = LoginForm()
        return render(request, "admin.html", {'form': form})


@login_required
def admin_logout(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return HttpResponseRedirect(Url.ADMIN.value)


@login_required
def admin_upload(request):
    if request.method == "POST":
        upload = UploadForm(request.POST, request.FILES)
        classroom = ClassroomForm(request.POST)
        if upload.is_valid():
            valid_extensions = [".csv", ".xlsx"]
            ext = os.path.splitext(request.FILES["csvFile"].name)[1]
            if ext not in valid_extensions:
                messages.error(request, "File type not allowed!")
            else:
                Planning.objects.all().delete()
                tmp_files = []
                file_path = handle_uploaded_file(request.FILES["csvFile"], ext)
                tmp_files.append(file_path)
                if ext == valid_extensions[1]:
                    file_path = convert_xlsx_csv(file_path)
                    tmp_files.append(file_path)
                import_csv(file_path)
                delete_tmp_files(tmp_files)
                messages.success(request, "Upload successful")
        elif classroom.is_valid():
            today = datetime.datetime.today().strftime('%Y-%m-%d')
            for i in range(1, 6):
                data = Planning.objects.filter(date=today, grade=i).order_by("hour")
                for entry in data:
                    entry.classroom = classroom.cleaned_data[get_grade_by_id(i)]
                    entry.save()
    else:
        upload = UploadForm()
        classroom = ClassroomForm()
    return render(request, "upload.html", {"upload": upload, "classroom": classroom})


def delete_tmp_files(tmp_files):
    for file in tmp_files:
        try:
            os.remove(file)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


def convert_xlsx_csv(file):
    csv_file = "files/" + time.strftime("%Y%m%d%H%M%S") + ".csv"
    df = pd.read_excel(file)
    df.to_csv(csv_file, encoding="UTF-8", index=False)
    return csv_file


def import_csv(file):
    with open(file, encoding="utf8", errors="replace") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for index, row in enumerate(reader):
            if index > 0 and check_row(row):
                row = format_row(row)
                query = Planning()
                query.course_code = row[RowTarget.COURSE_CODE.value]
                query.date = dateparser.parse(row[RowTarget.DATE.value], languages=["fr"], date_formats=["%Y-%m-%d"])
                query.grade = row[RowTarget.GRADE.value]
                query.course_name = row[RowTarget.COURSE_NAME.value]
                query.teacher = row[RowTarget.TEACHER.value]
                query.hour = row[RowTarget.HOUR.value]
                query.duration = datetime.datetime(year=2000, month=1, day=1, hour=int(row[RowTarget.DURATION.value]), minute=0)
                query.exam_type = is_exam(row[RowTarget.COURSE_NAME.value])
                query.save()
    return True


def handle_uploaded_file(file, ext):
    try:
        os.makedirs("files")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    file_path = "files/" + time.strftime("%Y%m%d%H%M%S") + ext
    with open(file_path, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return file_path


def check_row(row):
    for element in row:
        if element == "":
            return False
        else:
            return True


def format_row(row):
    for i, col in enumerate(row):
        row[i] = row[i].upper()
        row[i] = row[i].replace("\"", "")
        row[i] = row[i].replace("'", "")
    return row


def is_exam(row):
    keywords_exam = {
        "QCM": "QCM",
        "TP": "TP",
        "SOE": "SOE",
        "MINI PROJET": "PROJECT",
        "POSITION TEST": "POSITION TEST"
    }
    for key, value in keywords_exam.items():
        if key in row:
            return value
    return ""


@login_required
def admin_delete(request):
    Planning.objects.all().delete()
    messages.success(request, "Planning emptied")
    return HttpResponseRedirect(Url.ADMIN_PLANNING_UPLOAD.value)
