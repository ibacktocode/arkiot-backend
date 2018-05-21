from users.serializers import SmsRequestOtpSerializer, SmsVerifyOtpSerializer
from rest_framework import views
from rest_framework.response import Response
from users.utils import SmsVerify
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
# Create your views here.

class SmsRequestOtpView(views.APIView):
    http_method_names = ['post']
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (IsAuthenticated, TokenHasReadWriteScope,)
    serializer_class = SmsRequestOtpSerializer

    def post(self, request, format=None):
        phone =  request.POST['phone']
        app_hash = request.POST['app_hash']

        serializer = SmsRequestOtpSerializer(
            {
                'otp': SmsVerify().request_code(phone=phone, app_hash=app_hash)
            }
        )
        return Response(serializer.data)

class SmsVerifyOtpView(views.APIView):
    http_method_names = ['post']
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (IsAuthenticated, TokenHasReadWriteScope,)
    serializer_class = SmsVerifyOtpSerializer

    def post(self, request, format=None):
        phone =  request.POST['phone']
        app_hash = request.POST['app_hash']
        otp = request.POST['otp']

        serializer = SmsVerifyOtpSerializer(
            {
                'status': SmsVerify().verify_code(phone=phone, app_hash=app_hash, otp=otp)
            }
        )
        return Response(serializer.data)