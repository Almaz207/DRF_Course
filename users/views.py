from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from users.models import Payments

from users.serializers import PaymentsSerializer


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
