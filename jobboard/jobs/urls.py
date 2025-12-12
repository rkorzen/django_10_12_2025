from django.urls import path
from . import views

app_name = "jobs"
urlpatterns = [
    # / strona glowna
    path("",  views.MyHomePageView.as_view(), name="home"),
    path(app_name, views.list, name="list"),
    path(f"{app_name}/<int:id>", views.detail, name="detail"),
    path(f"{app_name}/add", views.add, name="create"),
    path("about", views.about),
    path("contact", views.contact, name="contact"),
]
