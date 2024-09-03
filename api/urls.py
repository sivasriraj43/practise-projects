from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet,registerview

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'books',BookViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('register',registerview,name='register'),
    path('login/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]