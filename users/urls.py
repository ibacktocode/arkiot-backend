from django.conf.urls import url
from users.views import SmsRequestOtpViewSet

urlpatterns = [
    url(r'^request-otp/$', SmsRequestOtpViewSet.as_view({'post': 'retrieve'}),name='request-otp'),
]
