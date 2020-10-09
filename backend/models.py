from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Appliance_list(models.Model):
    user = models.ForeignKey(User, related_name="appliances", on_delete=models.CASCADE)
    TVs_num = models.CharField(max_length=255, default="0")
    Decoders_num = models.CharField(max_length=255, default="0")
    SoundSystems_num = models.CharField(max_length=255, default="0")
    Lights_num = models.CharField(max_length=255, default="0")
    Heaters_num = models.CharField(max_length=255, default="0")
    Stoves_num = models.CharField(max_length=255, default="0")
    Fridges_num = models.CharField(max_length=255, default="0")
    Kettles_num = models.CharField(max_length=255, default="0")
    Microwaves_num = models.CharField(max_length=255, default="0")
    Computers_num = models.CharField(max_length=255, default="0")
    Printers_num = models.CharField(max_length=255, default="0")
    Modems_num = models.CharField(max_length=255, default="0")
    ElectricBlankets_num = models.CharField(max_length=255, default="0")
    Phones_num = models.CharField(max_length=255, default="0")

    def serialize(self):
        return {
            'id':self.id,
            'user_id':self.user.id,
            'TVs_num':self.TVs_num,
            'Decoders_num':self.Decoders_num,
            'SoundSystems_num':self.SoundSystems_num,
            'Lights_num':self.Lights_num,
            'Heaters_num':self.Heaters_num,
            'Stoves_num':self.Stoves_num,
            'Fridges_num':self.Fridges_num,
            'Kettles_num':self.Kettles_num,
            'Microwaves_num':self.Microwaves_num,
            'Computers_num':self.Computers_num,
            'Printers_num':self.Printers_num,
            'Modems_num':self.Modems_num ,
            'ElectricBlankets_num':self.ElectricBlankets_num,
            'Phones_num':self.Phones_num
        }




