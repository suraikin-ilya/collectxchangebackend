# Generated by Django 4.2 on 2023-05-04 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_country_preservation_delete_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]