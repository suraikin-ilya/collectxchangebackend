# Generated by Django 4.2 on 2023-05-15 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0046_item_country_item_preservation_item_trade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='country',
        ),
        migrations.RemoveField(
            model_name='item',
            name='preservation',
        ),
    ]
