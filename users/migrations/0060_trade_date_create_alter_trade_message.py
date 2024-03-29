# Generated by Django 4.2 on 2023-05-30 13:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0059_trade'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='date_create',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trade',
            name='message',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
