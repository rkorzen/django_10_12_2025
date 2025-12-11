from http.cookiejar import HEADER_JOIN_TOKEN_RE

from django.shortcuts import render
from django.http import HttpResponse

from tags.models import Tag
from .models import Offer


def home_view(request):
    return HttpResponse("Hello Worlsdsdsdd!")


from django.template.loader import render_to_string


def list(request):
    # pobieram z bazy
    # print(dir(request))
    # print(request.GET)

    tag = request.GET.get("tag")
    q = request.GET.get("q")

    if tag:
        offers = Offer.objects.filter(tags__name__iexact=tag)  # tags.name == tag
    else:
        offers = Offer.objects.all()

    if q:
        offers = offers.filter(title__icontains=q)
    tags = Tag.objects.all()

    context = {
        "offers": offers,
        "text": "to jest jakios tekst",
        "lista": [1, 2, 3, 4],
        "slownik": {"a": "aaa", "b": "bbb"},
        "tags": tags

    }

    # rendered = render_to_string("jobs/lista.html", context)
    # return HttpResponse(rendered)
    return render(
        request,
        "jobs/list.html",
        context
    )


def detail(request, id):
    # offer = [x for x in baza if x.id == id]
    # context = {"offer": offer[0]}

    offer = Offer.objects.get(id=id)
    context = {"offer": offer}
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
