from random import choice

from django.core.management.base import BaseCommand, CommandError

from ...factories import PositionFactory


class Command(BaseCommand):
    help = 'Create Positions'

    def handle(self, *args, **options):
        print "Creating Positions"

        titles = ('Header', 'Aside', 'Feature', 'Footer')

        for title in titles:
            PositionFactory(title=title)
            print "Added Position: {}".format(title)
