import os
import django

# Установка переменной окружения для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from users.models import Preservation

def seed_preservation():
    preservation_choices = [
        (Preservation.PF, 'Proof'),
        (Preservation.PL, 'Proof-like'),
        (Preservation.BU, 'Brilliant Uncirculated'),
        (Preservation.UNC, 'Uncirculated'),
        (Preservation.AUP, 'Choice Almost/About Uncirculated'),
        (Preservation.AU, 'Almost/About Uncirculated'),
        (Preservation.XFP, 'Choice Extremely Fine'),
        (Preservation.XF, 'Extremely Fine'),
        (Preservation.VFP, 'Choice Very Fine'),
        (Preservation.VF, 'Very Fine'),
        (Preservation.F, 'Fine'),
        (Preservation.VG, 'Very Good'),
        (Preservation.G, 'Good'),
        (Preservation.AG, 'Almost/About Good'),
        (Preservation.FA, 'Fair'),
        (Preservation.PR, 'Poor'),
    ]

    for choice in preservation_choices:
        preservation = Preservation(category=choice[0])
        preservation.save()
        print(f'Seeded preservation: {preservation.get_category_display()}')

if __name__ == '__main__':
    seed_preservation()
