from django.core.management.base import BaseCommand

from ...models import Position


class Command(BaseCommand):
    help = 'Clean up Footer'

    def handle(self, *args, **options):
        Position.objects.delete()
