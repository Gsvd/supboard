import datetime
from datetime import date

from django.shortcuts import render

from .models import Planning


def planning(request, year=0, month=0, day=0):
    if 2000 <= int(year) <= 2100 and 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
        date_planning = date(int(year), int(month), int(day))
    else:
        date_planning = datetime.datetime.now()
    plannings = [
                Planning.objects.filter(date=date_planning, grade=1).order_by("hour"),
                Planning.objects.filter(date=date_planning, grade=2).order_by("hour"),
                Planning.objects.filter(date=date_planning, grade=3).order_by("hour"),
                Planning.objects.filter(date=date_planning, grade=4).order_by("hour"),
                Planning.objects.filter(date=date_planning, grade=5).order_by("hour")
                ]
    datas = {
        "plannings": plannings
    }
    return render(request, "planning.html", datas)
