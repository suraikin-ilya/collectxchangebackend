from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, CollectionSerializer, CategorySerializer, ItemSerializer, PreservationSerializer, CountrySerializer, TradeSerializer
from rest_framework.response import Response
from .models import User, Collection, Category, Preservation, Country, Item, Trade, Chat
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework import generics
from django.db.models import Q
from .pusher import pusher_client
from django.utils import timezone
from django.http import HttpResponseBadRequest

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError({"email": ["Пользователь с таким email уже существует"]})

        nickname = serializer.validated_data.get("nickname")
        if User.objects.filter(nickname=nickname).exists():
            raise ValidationError({"nickname": ["Данный nickname уже занят"]})

        # Получение аватара из запроса
        avatar = request.FILES.get('avatar')
        if avatar:
            serializer.validated_data['avatar'] = avatar

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
            serializer.save(owner = request.data['owner'])
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

    def patch(self, request, pk, format=None):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            item = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item)
        return Response(serializer.data)

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

class CollectionItemCountAPIView(APIView):
    def get(self, request, collection_id):
        item_count = Item.objects.filter(collection=collection_id).count()
        return Response({'item_count': item_count})

class CollectionByViewsAPIView(APIView):
    def get(self, request):
        collections = Collection.objects.order_by('-views')
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)

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

class IncreaseViewsAPIView(APIView):
    def post(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
            item.views += 1
            item.save()
            return Response({'message': 'Views increased successfully.'}, status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)

class IncreaseCollectionViewsAPIView(APIView):
    def post(self, request, collection_id):
        try:
            collection = Collection.objects.get(id=collection_id)
            collection.views += 1
            collection.save()
            return Response({'message': 'Views increased successfully.'}, status=status.HTTP_200_OK)
        except Collection.DoesNotExist:
            return Response({'error': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)

class ItemListView(APIView):
    def get(self, request):
        items = Item.objects.order_by('-date_create')
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class GetOwner(APIView):
    def get(self, request, item_owner):
        try:
            user = User.objects.get(id=item_owner)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class VisibleItemsView(APIView):
    def get(self, request):
        items = Item.objects.filter(visibility=True)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class VisibleItemsByOwnerView(APIView):
    def get(self, request, owner_key):
        items = Item.objects.filter(owner=owner_key, visibility=True)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class UserIdView(APIView):
    def get(self, request, nickname):
        try:
            user = User.objects.get(nickname=nickname)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

class TradeItemsByOwnerView(APIView):
    def get(self, request, owner_key):
        items = Item.objects.filter(owner=owner_key, visibility=True, trade=True)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class TradeAPIView(APIView):
    def post(self, request):
        serializer = TradeSerializer(data=request.data)
        if serializer.is_valid():
            trade = serializer.save()
            return Response({'trade_id': trade.id}, status=201)
        return Response(serializer.errors, status=400)

class TradeListAPIView(APIView):
    def get(self, request, userId):
        trades = Trade.objects.filter(user_to = userId)
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)

class TradeToggleStatusTrueAPIView(APIView):
    def put(self, request, trade_id):
        try:
            trade = Trade.objects.get(id=trade_id)
            if trade.status is None:
                trade.status = True  # Изменяем значение на 1 вместо 0
                trade.save()
                return Response({'message': 'Status toggled successfully.'})
            else:
                return Response({'message': 'Status is already set.'})
        except Trade.DoesNotExist:
            return Response({'message': 'Trade not found.'}, status=404)

class TradeToggleStatusFalseAPIView(APIView):
    def put(self, request, trade_id):
        try:
            trade = Trade.objects.get(id=trade_id)
            if trade.status is None:
                trade.status = False
                trade.save()
                return Response({'message': 'Status toggled successfully.'})
            else:
                return Response({'message': 'Status is already set.'})
        except Trade.DoesNotExist:
            return Response({'message': 'Trade not found.'}, status=404)

class TradeCountAPIView(APIView):
    def get(self, request, userId):
        count = Trade.objects.filter(status__isnull=True, user_to=userId).count()
        return Response({'trade_count': count})

class AllTradeListAPIView(APIView):
    def get(self, request, userId):
        trades = Trade.objects.filter(Q(user_to=userId) | Q(user_from=userId))
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)


class MessageAPIView(APIView):
    # получите данные из запроса (тело сообщения, получатель и т.д.)
    def post(self, request):
        body = request.data['body']
        recipient = request.data['recipient']
        sender = request.data['sender']

        # создайте объект модели Chat и сохраните его в базу данных
        chat = Chat(sender=sender, recipient=recipient, body=body)
        chat.save()

        timestamp = chat.timestamp.timestamp()  # Получите метку времени в формате Unix

        # отправьте событие "new-message" на канал Pusher
        pusher_client.trigger('chat', 'new-message', {'message': chat.body, 'timestamp': timestamp, 'sender': chat.sender, 'recipient': chat.recipient})

        return JsonResponse({'status': 'success'})


class GetMessagesAPIView(APIView):
    # получите все сообщения, у которых sender или recipient равны username
    def get(self, request, username):
        messages = Chat.objects.filter(Q(sender=username) | Q(recipient=username))

        # преобразуйте сообщения в список словарей
        messages_list = [
            {
                'sender': message.sender,
                'recipient': message.recipient,
                'body': message.body,
                'timestamp': message.timestamp
            }
            for message in messages
        ]

        return JsonResponse({'messages': messages_list})

class GetChatAPIView(APIView):
    def get(self, request, username, another_username):
        messages = Chat.objects.filter(
            Q(sender=username, recipient=another_username) | Q(sender=another_username, recipient=username)
        )

        messages_list = [
            {
                'sender': message.sender,
                'recipient': message.recipient,
                'body': message.body,
                'timestamp': message.timestamp
            }
            for message in messages
        ]

        return JsonResponse({'messages': messages_list})


class AvatarView(APIView):
    def get(self, request, nickname):
        user = get_object_or_404(User, nickname=nickname)
        if not user.avatar:
            return HttpResponseBadRequest("User has no avatar.")

        avatar_url = user.avatar.url
        return Response({"avatar_url": avatar_url})