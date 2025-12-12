from django.urls import path

from . import views
urlpatterns = [
    path("", views.api_root, name="index"),
    path("snippets/", views.SnippetList.as_view(), name="snippets-list"),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view(), name="snippet-detail"),
    path("snippets/<int:pk>/highlight/", views.SnippetHighlight.as_view(), name="snippet-highlight"),

    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),

]

# urlpatterns = format_suffix_patterns(urlpatterns)