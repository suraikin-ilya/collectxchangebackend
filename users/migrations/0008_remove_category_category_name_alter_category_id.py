# Generated by Django 4.2 on 2023-05-04 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_category_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_name',
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]