from django.core.management.base import BaseCommand

from jobs.factories import OfferFactory


class Command(BaseCommand):
    help = "Tworzy dane testowe ofert"

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        n = options['n']
        OfferFactory.create_batch(n)
        print(f"Utworzono {n} ofert")
