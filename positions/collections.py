from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection

from .models import Position
from .serializers import PositionSerializer


class PositionDocumentCollection(DRFDocumentCollection):
    model = Position
    serializer_class = PositionSerializer
    name = 'economica__positions'


mongodb.register(PositionDocumentCollection())
