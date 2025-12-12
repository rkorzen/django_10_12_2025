from django.urls import path
from . import views

app_name = "todos"
urlpatterns = [
    path(app_name, views.TodoListView.as_view(), name="list"),
    path(f"{app_name}/<int:id>", views.detail, name="detail"),
    path(f"{app_name}/add", views.add),
]
