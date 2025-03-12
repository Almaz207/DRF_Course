from rest_framework.routers import SimpleRouter
from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentsViewSet, PaymentsListAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register("payments", PaymentsViewSet)

urlpatterns = [
    path("all_payments/", PaymentsListAPIView.as_view(), name='all_payments')
]

urlpatterns += router.urls
