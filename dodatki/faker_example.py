import faker
from pprint import pprint
fake_en = faker.Faker()
fake_pl = faker.Faker("pl_PL")

pprint(fake_en.name())
print(fake_en.address())
print(fake_en.text(max_nb_chars=100))
pprint(fake_pl.name())
pprint(fake_pl.address())
print(fake_pl.text(max_nb_chars=100))

data = [("a", "A"), ("b", "B")]
print(fake_pl.random_choices(data), 1)
fake_pl.random_choices()