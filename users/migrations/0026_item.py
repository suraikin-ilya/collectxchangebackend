# Generated by Django 4.2 on 2023-05-04 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_country_code_alter_country_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('trade', models.BooleanField()),
                ('date_create', models.DateField()),
                ('collection', models.IntegerField()),
                ('price', models.IntegerField()),
                ('WWC', models.CharField(default='', max_length=50)),
                ('CBRF', models.CharField(default='', max_length=50)),
                ('catalog_number', models.CharField(default='', max_length=50)),
                ('material', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('weight', models.FloatField()),
                ('obverse', models.BinaryField()),
                ('reverse', models.BinaryField()),
                ('extra_photo', models.BinaryField()),
                ('description', models.CharField(max_length=5000)),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('ISSN', models.CharField(default='', max_length=50)),
                ('date_publish', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.category')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.country')),
                ('preservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.preservation')),
            ],
        ),
    ]
