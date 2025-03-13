from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from users.models import Payment, CustomUser

from users.serializers import PaymentsSerializer, CustomUserSerializer


class PaymentsViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ('payment_course', 'payment_lesson', 'payment_method')
    ordering_fields = ('payment_time',)


class CustomUserCreatAPIView():
    pass
