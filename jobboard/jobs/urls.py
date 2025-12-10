from django.urls import path
from .views import home_view, offers_list, offer_detail, offer_add, about, contact

app_name = "jobs"
urlpatterns = [
    # / strona glowna
    path("",  home_view),
    path("offers", offers_list, name="list"),
    path("offers/<int:id>", offer_detail, name="detail"),
    path("offers/add", offer_add),
    path("about", about),
    path("contact", contact),
]
