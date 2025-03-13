from rest_framework.serializers import ModelSerializer

from users.models import CustomUser, Payment


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
