import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model
from .models import Offer, RecruiterProfile, Company


User = get_user_model()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class RecruiterProfileFactory(DjangoModelFactory):
    class Meta:
        model = RecruiterProfile

    user = factory.SubFactory(UserFactory)
    bio = factory.Faker('paragraph')
    phone_number = factory.Faker('phone_number')
    email = factory.Faker('email')


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker('company')
    website = factory.Faker('url')
    size = factory.Faker('random_int', min=1, max=1000000)

class OfferFactory(DjangoModelFactory):
    class Meta:
        model = Offer

    title = factory.Faker('job')
    description = factory.Faker('paragraph')
    is_published = factory.Faker('boolean')
    recruiter = factory.SubFactory(UserFactory)
    company = factory.SubFactory(CompanyFactory)
