import logging


from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from tags.models import Tag
from .forms import ContactForm
from .models import Offer


logger = logging.getLogger(__name__)

def home_view(request):
    return HttpResponse("Hello Worlsdsdsdd!")


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
    page_number = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 10)
    p = Paginator(offers, per_page)
    page = p.page(page_number)

    context = {
        "offers": page,
        "per_page": per_page,
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
    print(request.method)
    print(request.POST)
    form = ContactForm()

    if request.method == "POST":

        email = request.POST.get("email")
        content = request.POST.get("content")

        form = ContactForm(request.POST)
        if form.is_valid():

            body = f"Wiadomość od {email}: {content}"

            send_mail(
                "Nowa wiadomość od strony kontaktowej",
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL,]
            )

            logger.info("Wyslano emaila ze strony kontaktowej: {} {}".format(email, content))

        else:
            print(form.errors)
    return render(
        request,
        "contact.html",
        {"form": form}
    )
