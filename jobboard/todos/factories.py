import factory
from factory.django import DjangoModelFactory

from .models import Category, Todo


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    slug = factory.Faker('slug')


class TodoFactory(DjangoModelFactory):
    class Meta:
        model = Todo

    title = factory.Faker('sentence')
    description = factory.Faker('paragraph')
    start_date = factory.Faker('date_time_this_year')
    end_date = factory.Faker('date_time_this_year')
    category = factory.SubFactory(CategoryFactory)
    status = factory.Faker('random_element', elements=[x[0] for x in Todo.STATUS_CHOICES])



