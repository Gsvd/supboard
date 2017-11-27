from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.admin_index, name="admin"),
    url(r"^logout/$", views.admin_logout, name="logout"),
    url(r"^planning/upload/$", views.admin_upload, name="planning_upload"),
    url(r"^planning/delete/$", views.admin_delete, name="planning_delete"),
]
