# Generated by Django 4.2 on 2023-05-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0039_alter_item_date_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='CBRF',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='ISSN',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='WWC',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='catalog_number',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='country',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='extra_photo',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
        migrations.AlterField(
            model_name='item',
            name='height',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='material',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='obverse',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
        migrations.AlterField(
            model_name='item',
            name='preservation',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='reverse',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
        migrations.AlterField(
            model_name='item',
            name='weight',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='width',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='year',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
