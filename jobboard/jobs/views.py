from django.shortcuts import render
from django.http import HttpResponse
from .models import baza
# Create your views here.
def home_view(request):
    return HttpResponse("Hello Worlsdsdsdd!")

#
# def offers_list(request):
#     offers = baza
#
#     text = """
#     <!doctype html>
#     <html>
#     <head></head>
#     <body>
#     Offers list<br>"""
#
#     for offer in offers:
#         text += f"{offer.title} {offer.description}<br>"
#
#     text += "</body></html>"
#     return HttpResponse(text)


def offers_list(request):
    # pobieram z bazy
    offers = baza

    return render(
        request,
        "jobs/lista.html",
        {"offers": offers}
    )

def offer_detail(request, id):
    return HttpResponse(f"Szczegoly oferty: {id}")

def offer_add(request):
    return HttpResponse("Dodanie oferty")

def about(request):
    return HttpResponse("O nas")

def contact(request):
    return HttpResponse("Kontakt")
