# Generated by Django 5.0.3 on 2024-04-26 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('darabala', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parent',
            options={},
        ),
        migrations.RemoveField(
            model_name='parent',
            name='password',
        ),
    ]