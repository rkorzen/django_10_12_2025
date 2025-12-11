import contextlib
from io import StringIO

from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch

from tags.factories import TagFactory
from tags.models import Tag
from .factories import OfferFactory, CompanyFactory, UserFactory
from .models import Offer


class OfferModelTest(TestCase):

    def setUp(self):
        self.company = CompanyFactory(name="ACME Corp", website="https://acme.com")
        self.user = UserFactory(username="johndoe", email="johndoe@company.net")

    def test_offer_str(self):
        offer = OfferFactory(title="Software Engineer", company=self.company)
        self.assertEqual(str(offer), offer.title)

    def test_offer_info(self):
        offer = OfferFactory(title="Software Engineer", description="ABC", company=self.company)
        self.assertEqual(offer.info(), f"{offer.title} {offer.description}")

    def test_offer_related_tags_are_accessible(self):
        offer = OfferFactory(title="Software Engineer", description="ABC", company=self.company)
        python_tag = TagFactory(name="Python")
        data_tag = TagFactory(name="Data")

        offer.tags.add(python_tag, data_tag)

        self.assertIn(python_tag, offer.tags.all())
        self.assertIn(data_tag, offer.tags.all())

        self.assertQuerySetEqual(
            offer.tags.order_by("name"),
            Tag.objects.order_by("name"),
        )


class OfferViewsTests(TestCase):
    def setUp(self):
        self.python_offer = OfferFactory(title="Python Developer", description="ABC")
        self.ruby_offer = OfferFactory(title="Ruby on Rails Developer", description="ABC")

    def test_offer_list_view(self):
        response = self.client.get(reverse("jobs:list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "jobs/list.html")
        self.assertContains(response, self.python_offer.info())
        self.assertContains(response, self.ruby_offer.info())


    def test_offer_filter_query_view(self):

        response = self.client.get(reverse("jobs:list") + "?q=python")
        self.assertContains(response, self.python_offer.info())
        self.assertNotContains(response, self.ruby_offer.info())


class CreateJobCommandTests(TestCase):

    @patch("jobs.management.commands.create_jobs.OfferFactory")
    def test_command_creates_requested_number_of_offers(self, mock_factory):
        stdout = StringIO()
        with contextlib.redirect_stdout(stdout):
            call_command("create_jobs", "3")

        mock_factory.create_batch.assert_called_once_with(3)

        self.assertIn("Utworzono 3 ofert", stdout.getvalue())
