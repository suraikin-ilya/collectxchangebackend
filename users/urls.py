from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import RegisterView, LoginView, UserView, LogoutView, CollectionView, GetCollectionView, \
    GetCollectionItemView, CategoryAPIView, ItemAPIView, PreservationAPIView, CountryAPIView, ItemListAPIView, \
    ItemDeleteAPIView, ToggleTradeAPIView, ToggleVisibilityAPIView, GetItemRetrieveAPIView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('collections', CollectionView.as_view()),
    path('collections/<int:id>/', CollectionView.as_view()),
    path('collections/get/<int:owner>/', GetCollectionView.as_view()),
    path('collection/<int:id>/', GetCollectionItemView.as_view()),
    path('categories/', CategoryAPIView.as_view()),
    path('item/', ItemAPIView.as_view()),
    path('preservations/', PreservationAPIView.as_view()),
    path('countries/', CountryAPIView.as_view()),
    path('items/collection/<int:collection_id>/', ItemListAPIView.as_view()),
    path('items/<int:pk>/delete/', ItemDeleteAPIView.as_view()),
    path('items/<int:pk>/toggle-trade/', ToggleTradeAPIView.as_view()),
    path('items/<int:pk>/toggle-visibility/', ToggleVisibilityAPIView.as_view()),
    path('item/<int:pk>/', GetItemRetrieveAPIView.as_view(), name='item-retrieve'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

