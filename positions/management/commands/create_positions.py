from random import choice

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from menus.models import Link

from ...factories import PositionFactory


class Command(BaseCommand):
    help = 'Create Positions'

    def handle(self, *args, **options):
        print "Creating Positions"

        titles = ('Header', 'Aside', 'Feature', 'Footer')
        links = Link.objects.all()

        if not links.exists():
            call_command('create_menus')

        for title in titles:
            random_links = []

            for j in range(3):
                random_links.append(choice(links))

            PositionFactory(title=title, links=random_links)
            print "Added Position: {}".format(title)
