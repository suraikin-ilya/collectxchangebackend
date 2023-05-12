# Generated by Django 4.2 on 2023-05-08 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_alter_item_cbrf_alter_item_issn_alter_item_wwc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Монета', 'Монета'), ('Банкнота', 'Банкнота'), ('Значок', 'Значок'), ('Видеоигра', 'Видеоигра'), ('Почтовая марка', 'Почтовая марка'), ('Журнал', 'Журнал'), ('Другое', 'Другое')], default='Другое', max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]