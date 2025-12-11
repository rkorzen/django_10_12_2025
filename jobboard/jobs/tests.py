from django.test import TestCase

from tags.factories import TagFactory
from tags.models import Tag
from .factories import OfferFactory, CompanyFactory, UserFactory


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