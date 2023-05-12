import os
import yaml
import codecs

from django.core.management.base import BaseCommand
from users.models import Country


class Command(BaseCommand):
    help = 'Loads data about countries from YAML file'

    def handle(self, *args, **options):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        yaml_file = os.path.join(base_dir, 'countries.yaml')

        with codecs.open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        for code, name in data['countries'].items():
            country, _ = Country.objects.get_or_create(code=code)
            country.name = name
            country.save()

        self.stdout.write(self.style.SUCCESS('Data about countries has been successfully loaded.'))
