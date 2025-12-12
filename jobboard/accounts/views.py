from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class MyLoginView(LoginView):
    template_name = "accounts/login.html"


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("jobs:list")
