import factory

from django.contrib.webdesign.lorem_ipsum import paragraphs, words

from faker import Factory


fake = Factory.create()


class PositionFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'positions.Position'

    title = factory.LazyAttribute(lambda o: words(2, common=False).title())
