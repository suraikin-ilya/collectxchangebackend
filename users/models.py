from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    visibility = models.BooleanField()
    owner = models.IntegerField()
    views = models.IntegerField(default='0')
    created_date = models.DateField(auto_now_add=True)

class Category(models.Model):
     COIN = 'Монета'
     BANKNOTE = 'Банкнота'
     PIN = 'Значок'
     VIDEOGAME = 'Видеоигра'
     POST_STAMP = 'Почтовая марка'
     MAGAZINE = 'Журнал'
     OTHER = 'Другое'
     CATEGORIES = [
         (COIN, 'Монета'),
         (BANKNOTE, 'Банкнота'),
         (PIN, 'Значок'),
         (VIDEOGAME, 'Видеоигра'),
         (POST_STAMP, 'Почтовая марка'),
         (MAGAZINE, 'Журнал'),
         (OTHER, 'Другое'),
     ]
     category = models.CharField(
         max_length=20,
         choices=CATEGORIES,
         default=OTHER,
     )




class Preservation(models.Model):
    PF = 'PF'
    PL = 'PL'
    BU = 'BU'
    UNC = 'UNC'
    AUP = 'AU+'
    AU = 'AU'
    XFP = 'XF+'
    XF = 'XF'
    VFP = 'VF+'
    VF = 'VF'
    F = 'F'
    VG = 'VG'
    G = 'G'
    AG = 'AG'
    FA = 'FA'
    PR = 'PR'
    PRESERVATION_CHOICES = [
        (PF, 'Proof'),
        (PL, 'Proof-like'),
        (BU, 'Brilliant Uncirculated'),
        (UNC, 'Uncirculated'),
        (AUP, 'Choice Almost/About Uncirculated'),
        (AU, 'Almost/About Uncirculated'),
        (XFP, 'Choice Extremely Fine'),
        (XF, 'Extremely Fine'),
        (VFP, 'Choice Very Fine'),
        (VF, 'Very Fine'),
        (F, 'Fine'),
        (VG, 'Very Good'),
        (G, 'Good'),
        (AG, 'Almost/About Good'),
        (FA, 'Fair'),
        (PR, 'Poor'),
    ]
    category = models.CharField(
        max_length=3,
        choices=PRESERVATION_CHOICES,
        default=VF,
    )

    def __str__(self):
        return self.get_category_display()

#
class Country(models.Model):
    code = models.CharField(max_length=2, unique=True, default='')
    name = models.TextField(default='')




class Item(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.IntegerField()
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='',blank=True)
    trade = models.BooleanField()
    visibility = models.BooleanField()
    date_create = models.DateField(auto_now_add=True)
    collection = models.IntegerField()
    price = models.IntegerField(blank=True)
    WWC = models.CharField(max_length=50, default='',blank=True)
    CBRF = models.CharField(max_length=50, default='',blank=True)
    catalog_number = models.CharField(max_length=50, default='',blank=True)
    material = models.CharField(max_length=100,blank=True, default='')
    year = models.IntegerField(blank=True, default='')
    weight = models.FloatField(blank=True, default='')
    preservation = models.CharField(max_length=50, default='',blank=True)
    country = models.CharField(max_length=50, default='',blank=True)
    obverse = models.ImageField(upload_to='item_images',blank=True)
    reverse = models.ImageField(upload_to='item_images',blank=True)
    extra_photo = models.ImageField(upload_to='item_images',blank=True)
    description = models.CharField(max_length=5000)
    width = models.FloatField(blank=True)
    height = models.FloatField(blank=True)
    ISSN = models.CharField(max_length=50, default='',blank=True)
    date_publish = models.DateField(blank=True)

    def __str__(self):
        return self.name
