from rest_framework.serializers import Serializer, CharField
from users.models import Sms
class SmsRequestOtpSerializer(Serializer):
    otp = CharField(read_only=True, max_length=10)

    # def create(self, validated_data):
    #     return Sms(validated_data)