import factory

from django.contrib.webdesign.lorem_ipsum import paragraphs, words

from faker import Factory


fake = Factory.create()


class PositionFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'positions.Position'
    FACTORY_DJANGO_GET_OR_CREATE = ('title', )

    title = factory.LazyAttribute(lambda o: words(2, common=False).title())

    @factory.post_generation
    def links(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for link in extracted:
                self.links.add(link)
