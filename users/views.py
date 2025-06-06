from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from users.models import Payment, CustomUser

from users.serializers import PaymentsSerializer, CustomUserSerializer
from users.services import (
    create_stripe_product,
    create_stripe_price,
    create_stripe_session,
)


class PaymentsViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ("payment_course", "payment_lesson", "payment_method")
    ordering_fields = ("payment_time",)


class PaymentCreateAPIView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentsSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        payment.user = self.request.user
        stripe_product = create_stripe_product(instance=payment)
        stripe_price = create_stripe_price(amount=payment.price, product_id=stripe_product.id)
        session_id, payment_link = create_stripe_session(stripe_price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()


class CustomUserCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class CustomUserRetrieveAPIView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = []


class CustomUserUpdateAPIView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = []


class CustomUserDestroyAPIView(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = []
