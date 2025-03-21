from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import (
    PaymentsViewSet,
    PaymentsListAPIView,
    CustomUserCreateAPIView,
    PaymentCreateAPIView,
)

app_name = UsersConfig.name

router = SimpleRouter()
router.register("payments", PaymentsViewSet)

urlpatterns = [
    path("register/", CustomUserCreateAPIView.as_view(), name="register"),
    path("all_payments/", PaymentsListAPIView.as_view(), name="all_payments"),
    path("api/token/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="token"),
    path("api/token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
    path("payment/create/", PaymentCreateAPIView.as_view(), name="create_payment"),
]

urlpatterns += router.urls
