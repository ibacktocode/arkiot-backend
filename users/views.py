from users.serializers import SmsRequestOtpSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from users.utils import SmsVerify
# Create your views here.

class SmsRequestOtpViewSet(viewsets.ViewSet):
    serializer_class = SmsRequestOtpSerializer

    def retrieve(self, request, pk=None):
        serializer = SmsRequestOtpSerializer(
            {
                'otp': SmsVerify().request_code(phone='+84938038277', app_hash='1')
            }
        )
        return Response(serializer.data)
