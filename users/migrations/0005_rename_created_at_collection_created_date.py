# Generated by Django 4.2 on 2023-04-30 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_collection_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='created_at',
            new_name='created_date',
        ),
    ]
