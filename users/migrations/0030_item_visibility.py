# Generated by Django 4.2 on 2023-05-07 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_item_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='visibility',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
