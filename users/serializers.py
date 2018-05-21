from rest_framework.serializers import Serializer, CharField, BooleanField
from users.models import Sms
class SmsRequestOtpSerializer(Serializer):
    otp = CharField(read_only=True, max_length=10)

class SmsVerifyOtpSerializer(Serializer):
    status = BooleanField(read_only=True)