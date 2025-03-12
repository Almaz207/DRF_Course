from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from users.models import Payments

from users.serializers import PaymentsSerializer


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsListAPIView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ('payment_course', 'payment_lesson', 'payment_method')
    ordering_fields = ('payment_time',)
