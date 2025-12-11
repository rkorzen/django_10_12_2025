from django.core.paginator import Paginator
from pprint import pprint
objects = ["Pawel", "Rafal", "Karol", "Michal"]

p = Paginator(objects, 2)

print(p.count)

pprint(dir(p))


page = p.page(2)
for x in page: print(x)
print(page)

print(page.has_next())
print(page.has_previous())