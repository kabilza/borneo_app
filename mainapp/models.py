from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

# Create your models here.
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    brief_info = models.TextField('Background Infomation', default="NOT SET")
    phone_num = models.CharField('Phone Number', max_length=10, default="NOT SET")
    twitter = models.TextField('Twitter', default="NOT SET")
    facebook = models.TextField('Facebook', default="NOT SET")
    line = models.TextField('LINE', default="NOT SET")
    age =  models.CharField('Age', max_length=2, default="NOT SET")
    home_address = models.TextField('Home Address', default="NOT SET")
    home_postalcode = models.TextField('Home Postal Code', default="NOT SET")
    home_province = models.TextField('Home Province', default="NOT SET")
    home_district = models.TextField('Home District', default="NOT SET")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_brief_info(self):
        return self.brief_info

    def get_number(self):
        return self.phone_num

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)        

class BatteryWarranty(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    barcode = models.CharField('Barcode', default="NOT SET", max_length=13)
    brand = models.CharField('Battery Brand', default="NOT SET", max_length=20)
    battery_type = models.CharField('Battery Type', default="NOT SET", max_length=20)
    battery_model = models.CharField('Battery Model', default="NOT SET", max_length=20)
    warranty_period = models.CharField('Warranty Period', default="NOT SET", max_length=20)
    date_installed = models.DateField()
    shop_name = models.CharField('Shop Name', default="NOT SET", max_length=50)
    shop_province = models.CharField('Shop Province', default="NOT SET", max_length=20)
    shop_district = models.CharField('Shop District', default="NOT SET", max_length=20)
    shop_phonenumber = models.CharField('Shop Phone Number', default="NOT SET", max_length=11)

    def __str__(self):
        return f"{self.profile.user.first_name} {self.profile.user.last_name}"