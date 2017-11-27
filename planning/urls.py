from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$",
        views.planning, name="planning"),
    url(r"^date/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})/$",
        views.planning, name="planning_date")
]
