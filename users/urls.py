from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import RegisterView, LoginView, UserView, LogoutView, CollectionView, GetCollectionView, \
    GetCollectionItemView, CategoryAPIView, ItemAPIView, PreservationAPIView, CountryAPIView, ItemListAPIView

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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

