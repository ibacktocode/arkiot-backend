from twilio.rest import Client
import random
import redis
from django.conf import settings

class SmsVerify:

    def __init__(self, expiration_interval = 60):
        self.sender_phone = settings.TWILLIO_SENDER_PHONE
        self.twilio_client = Client(settings.TWILLIO_ACCOUNT, settings.TWILLIO_TOKEN)
        self.expiration_interval = expiration_interval
        
    def generate_otp(self, length=6):
        return str(random.randint(0, 10 ** length - 1)).zfill(length)

    def generate_key(self, phone, app_hash):
        return 'otp:' + phone + ':' + app_hash 

    def request_code(self, phone, app_hash, length = 6):
        otp = self.generate_otp(length=length)

        sms_message = "[#] {} is your ARKIOT verification code.\n #{}".format(otp, app_hash)

        OtpCaching().set_cache_otp(key=self.generate_key(phone, app_hash), otp=otp)
        self.twilio_client.messages.create(to=phone, from_=self.sender_phone, body = sms_message)

        return otp
        
      
    def verify_code(self, phone, app_hash, otp):
        return OtpCaching().get_cache_otp(self.generate_key(phone, app_hash)) == otp

    def reset_code(self, phone, app_hash):
        OtpCaching().delete_cache_otp(self.generate_key(phone, app_hash))


class OtpCaching:
    pool = redis.ConnectionPool(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        # db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD
    )
    r = redis.Redis(connection_pool=pool)

    def set_cache_otp(self, key, otp):
        self.r.set(key, otp, ex=60)

    def get_cache_otp(self, key):
        otp = self.r.get(key)
        if otp is not None:
            return otp.decode('ascii')

    def delete_cache_otp(self, key):
        return self.r.delete(key)