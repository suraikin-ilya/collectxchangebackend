from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, CollectionSerializer, CategorySerializer, ItemSerializer, PreservationSerializer, CountrySerializer
from rest_framework.response import Response
from .models import User, Collection, Category, Preservation, Country, Item
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework import generics

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('Пользователь не найден')

        if not user.check_password(password):
            raise AuthenticationFailed('Неверный пароль')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=600),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
        }

        return response

class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Неаутентифицированный')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Неаутентифицированный')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return  Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


class CollectionView(APIView):
    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner= request.data['owner'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        post = get_object_or_404(Collection, pk=id)
        serializer = CollectionSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        post = get_object_or_404(Collection, pk=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetCollectionView(APIView):
    def get(self, request, owner):
        if owner:
            queryset = Collection.objects.filter(owner=owner)
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)

class GetCollectionItemView(APIView):
    def get(self, request, id):
        try:
            collection_item = Collection.objects.get(id=id)
            serializer = CollectionSerializer(collection_item)
            return Response(serializer.data)
        except Collection.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemAPIView(APIView):
    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            item = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        collection_id = self.kwargs['collection_id']
        queryset = super().get_queryset()
        return queryset.filter(collection=collection_id)

class GetItemRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            serializer = ItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ItemDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ToggleTradeAPIView(APIView):
    def put(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            item.trade = not item.trade  # Переключаем значение trade
            item.save()
            serializer = ItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ToggleVisibilityAPIView(APIView):
    def put(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            item.visibility = not item.visibility  # Переключаем значение trade
            item.save()
            serializer = ItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PreservationAPIView(APIView):
    def get(self, request, format=None):
        preservations = Preservation.objects.all()
        serializer = PreservationSerializer(preservations, many=True)
        return Response(serializer.data)


class CountryAPIView(APIView):
    def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)