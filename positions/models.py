from django.db import models

from entropy.base import EnabledMixin, SlugUniqueMixin, TitleMixin
from cqrs.models import CQRSModel


class Position(CQRSModel, EnabledMixin, SlugUniqueMixin, TitleMixin):
    '''
    A Position is a identifiable marker for position within a template where
    Displays of content can be configured to appear.

    Positions can be uniquely correlated across Platforms and Menu Links.
    Whereas multiple Platforms and Links might be specified, we will take the
    intersection of those Displays that are configured to both Link and Platform.

    e.g.

    links = ['home', ]
    platforms = ['b2c', 'microsite', ]
    position = 'landing-feature'

    There's a little work to do on the template side, in django templates place:

        {% position 'feature' %}

    or Meteor / Handlebars:

        {{> position 'feature'}}

    whereas, the passed in parameter matches the Position.slug, and the necessary template
    helpers or tags are in place provide the right machinery to supply the Displays or Menus.

    Specifying platforms and links, either by inclusion or exclude (default) - limits the
    validity of the Position.

    '''

    # title
    # short_title
    # slug
    # enabled

    platforms = models.ManyToManyField(
        'platforms.Platform')

    links = models.ManyToManyField('menus.Link')

    exclude = models.BooleanField(
        default=True)
