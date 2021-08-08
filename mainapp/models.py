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

    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_brief_info(self):
        return self.brief_info

    def get_number(self):
        return self.phone_num

class BatteryWarranty(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    barcode = models.TextField('Barcode', default="NOT SET")
    brand = models.TextField('Battery Brand', default="NOT SET")
    battery_type = models.TextField('Battery Type', default="NOT SET")
    battery_model = models.TextField('Battery Model', default="NOT SET")
    warranty_period = models.TextField('Warranty Period', default="NOT SET")
    date_installed = models.DateTimeField()
    shop_name = models.TextField('Shop Name', default="NOT SET")
    shop_province = models.TextField('Shop Province', default="NOT SET")
    shop_district = models.TextField('Shop District', default="NOT SET")
    shop_phonenumber = models.TextField('Shop Phone Number', default="NOT SET")
