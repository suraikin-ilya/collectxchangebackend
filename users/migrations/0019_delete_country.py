# Generated by Django 4.2 on 2023-05-04 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_remove_country_alpha2_code_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Country',
        ),
    ]
