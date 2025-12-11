import factory
from factory.django import DjangoModelFactory

from .models import Tag

class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Faker('word')