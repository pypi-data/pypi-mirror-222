import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from netbox_topology_views.models import CoordinateGroup, Coordinate

class CoordinateGroupListTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    devices = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = CoordinateGroup
        fields = ('pk', 'id', 'name', 'description', 'devices')
        default_columns = ('name', 'description', 'devices')

class CoordinateListTable(NetBoxTable):
    group = tables.Column(
        linkify=True
    )

    device = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = Coordinate
        fields = ('pk', 'id', 'group', 'device', 'x', 'y')
        default_columns = ('id', 'group', 'device', 'x', 'y')

