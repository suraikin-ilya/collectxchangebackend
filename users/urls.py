from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import RegisterView, LoginView, UserView, LogoutView, CollectionView, GetCollectionView, \
    GetCollectionItemView, CategoryAPIView, ItemAPIView, PreservationAPIView, CountryAPIView, ItemListAPIView, \
    ItemDeleteAPIView, ToggleTradeAPIView, ToggleVisibilityAPIView, GetItemRetrieveAPIView, CollectionItemCountAPIView, \
    IncreaseViewsAPIView, IncreaseCollectionViewsAPIView, ItemListView, GetOwner, CollectionByViewsAPIView, \
    VisibleItemsView, VisibleItemsByOwnerView, UserIdView, TradeItemsByOwnerView

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
    path('item/<int:pk>/', GetItemRetrieveAPIView.as_view()),
    path('item/count/<int:collection_id>/', CollectionItemCountAPIView.as_view()),
    path('increase_item_views/<int:item_id>/', IncreaseViewsAPIView.as_view()),
    path('increase_collection_views/<int:collection_id>/', IncreaseCollectionViewsAPIView.as_view()),
    path('items/', ItemListView.as_view()),
    path('get_owner/<int:item_owner>/', GetOwner.as_view()),
    path('collections_by_views/', CollectionByViewsAPIView.as_view()),
    path('visible_items/', VisibleItemsView.as_view()),
    path('visible_items/<int:owner_key>/', VisibleItemsByOwnerView.as_view()),
    path('user/<str:nickname>/', UserIdView.as_view()),
    path('trade_items/<int:owner_key>/', TradeItemsByOwnerView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

