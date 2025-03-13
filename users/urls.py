from rest_framework.routers import SimpleRouter
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import PaymentsViewSet, PaymentsListAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register("payments", PaymentsViewSet)

urlpatterns = [
    path("all_payments/", PaymentsListAPIView.as_view(), name='all_payments'),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
