from django.db import models
from backend.models import BaseModel
import uuid
import devices.utils as utils

# Create your models here.
class Device(BaseModel):
    device_uuid = models.UUIDField(default=uuid.uuid1())
    device_name = models.CharField(max_length=500)
    device_type_id = models.ForeignKey('DeviceType', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        ins = super(Device, self).save(*args, **kwargs)
        utils.save_qr_code(str(self.device_uuid))

    class Meta:
        db_table = 'device'
        

class DeviceType(BaseModel):
    type_code = models.CharField(max_length=200)
    type_name = models.CharField(max_length=500)
    type_desc = models.TextField()

    class Meta:
        db_table = 'device_type'
