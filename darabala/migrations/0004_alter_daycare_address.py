# Generated by Django 5.0.4 on 2024-04-27 12:40

import geoposition.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('darabala', '0003_alter_daycare_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daycare',
            name='address',
            field=geoposition.fields.GeopositionField(default='48.7194, 66.5901', max_length=42),
        ),
    ]
