# Generated by Django 4.2 on 2023-05-08 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_alter_category_category_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='country',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='preservation',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
