from rest_framework import serializers
from .models import User, Collection, Category, Item, Preservation, Country
from rest_framework import generics
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname', 'email', 'password', 'date_joined']
        extra_kwargs = {
            'password':  {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name', 'description', 'visibility', 'owner', 'created_date', 'views']


class CategorySerializer(serializers.Serializer):
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

    category = serializers.ChoiceField(choices=CATEGORIES)

    def to_internal_value(self, data):
        return {'category': data}

    def to_representation(self, instance):
        return getattr(instance, 'category')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        extra_kwargs = {
            'price': {'required': False},
            'WWC': {'required': False},
            'CBRF': {'required': False},
            'catalog_number': {'required': False},
            'year': {'required': False},
            'weight': {'required': False},
            'preservation': {'required': False},
            'country': {'required': False},
            'obverse': {'required': False},
            'reverse': {'required': False},
            'extra_photo': {'required': False},
            'date_publish': {'required': False},
        }


class PreservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preservation
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'