from cqrs.serializers import CQRSSerializer

from menus.serializers import LinkSerializer

from .models import Position


class PositionSerializer(CQRSSerializer):
    links = LinkSerializer(many=True)

    class Meta:
        model = Position
        fields = (
            'id',
            'title',
            'slug',
            'links'
        )
