from django.conf.urls import url
from users.views import SmsRequestOtpView, SmsVerifyOtpView
from django.contrib.auth import login, logout
from users.backends import UserAuth

urlpatterns = [
    url(r'^request-otp/$', SmsRequestOtpView.as_view(),name='request-otp'),
    url(r'^verify-otp/$', SmsVerifyOtpView.as_view(),name='verify-otp'),
]
