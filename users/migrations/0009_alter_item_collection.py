# Generated by Django 4.2 on 2023-05-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_category_category_name_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='collection',
            field=models.IntegerField(),
        ),
    ]
