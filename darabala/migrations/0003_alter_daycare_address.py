# Generated by Django 5.0.4 on 2024-04-27 12:38

import geoposition.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('darabala', '0002_alter_parent_options_remove_parent_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daycare',
            name='address',
            field=geoposition.fields.GeopositionField(max_length=42),
        ),
    ]