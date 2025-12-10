from http.cookiejar import HEADER_JOIN_TOKEN_RE

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

from django.template.loader import render_to_string
def list(request):
    # pobieram z bazy
    offers = baza

    context = {
            "offers": offers,
            "text": "to jest jakios tekst",
            "lista": [1, 2, 3, 4],
            "slownik": {"a": "aaa", "b": "bbb"}

        }

    # rendered = render_to_string("jobs/lista.html", context)
    # return HttpResponse(rendered)
    return render(
        request,
        "jobs/list.html",
        context
    )

def detail(request, id):

    offer = [x for x in baza if x.id == id]

    context = {"offer": offer[0]}

    return render(
        request,
        "jobs/details.html",
        context
    )

def add(request):
    return HttpResponse("Dodanie oferty")

def about(request):
    return HttpResponse("O nas")

def contact(request):
    return HttpResponse("Kontakt")
