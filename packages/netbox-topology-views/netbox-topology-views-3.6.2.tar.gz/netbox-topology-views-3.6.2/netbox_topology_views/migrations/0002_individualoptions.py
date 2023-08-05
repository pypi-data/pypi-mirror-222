# Generated by Django 4.1.4 on 2023-03-19 14:13

from django.db import migrations, models
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0167_module_status'),
        ('extras', '0084_staging'),
        ('netbox_topology_views', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('user_id', models.IntegerField(null=True, unique=True)),
                ('ignore_cable_type', models.CharField(blank=True, max_length=255)),
                ('show_unconnected', models.BooleanField(default=False)),
                ('show_cables', models.BooleanField(default=False)),
                ('show_logical_connections', models.BooleanField(default=False)),
                ('show_single_cable_logical_conns', models.BooleanField(default=False)),
                ('show_circuit', models.BooleanField(default=False)),
                ('show_power', models.BooleanField(default=False)),
                ('show_wireless', models.BooleanField(default=False)),
                ('draw_default_layout', models.BooleanField(default=False)),
                ('preselected_device_roles', models.ManyToManyField(blank=True, db_table='netbox_topology_views_individualoptions_preselected_device', related_name='+', to='dcim.devicerole')),
                ('preselected_tags', models.ManyToManyField(blank=True, db_table='netbox_topology_views_individualoptions_preselected_tag', related_name='+', to='extras.tag')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
