# Generated by Django 4.2 on 2023-05-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0044_remove_item_cbrf_remove_item_issn_remove_item_wwc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='CBRF',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ISSN',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='WWC',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='catalog_number',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='height',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='material',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='weight',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='width',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='year',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]