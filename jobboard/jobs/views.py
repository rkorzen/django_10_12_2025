import logging
from pyexpat.errors import messages

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import messages
from tags.models import Tag
from .forms import ContactForm, OfferRegistrationForm, CreateOfferForm
from .models import Offer, Registration, Company

logger = logging.getLogger(__name__)


class MyHomePageView(TemplateView):
    template_name = "base.html"

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
    form = OfferRegistrationForm()

    if request.method == "POST":
        form = OfferRegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # szukam czy juz takie zgloszenie istnieje
            try:
                # uwaga - to jest tylko przyklad - tu jest duzo pulapek - mozna nadpisac czyjesz zgloszenie
                r = Registration.objects.get(offer=offer, email=instance.email)
                if instance.message:
                    r.message = instance.message
                    r.save()
            except Registration.DoesNotExist:
                instance.offer = Offer.objects.get(id=id)
                instance.save()
            messages.info(request, "Twoje zgłoszenie zostało zapisane.")

    context = {"offer": offer, "form": form}
    return render(
        request,
        "jobs/details.html",
        context
    )

@login_required
def add(request):

    form  = CreateOfferForm()
    if request.method == "POST":
        form = CreateOfferForm(request.POST)
        if form.is_valid():
            # company data
            company_name = form.cleaned_data["company_name"]
            website = form.cleaned_data["website"]
            size = form.cleaned_data["size"]

            company, created = Company.objects.get_or_create(name=company_name)

            if created:
                company.website = website
                company.size = size
                company.save()

                instance = form.save(commit=False)
                instance.company = company
                instance.save()
            else:
                # offer data
                form.save()

    return render(
        request=request,
        template_name="jobs/create.html",
        context={"form": form}
    )


class AboutPageView(TemplateView):
    template_name = "about.html"


def about(request):
    return render(request, "about.html")

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
                [settings.DEFAULT_FROM_EMAIL, ]
            )

            logger.info("Wyslano emaila ze strony kontaktowej: {} {}".format(email, content))

        else:
            print(form.errors)
    return render(
        request,
        "contact.html",
        {"form": form}
    )
