from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

# Create your models here.
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    brief_info = models.CharField('Background Infomation', default="NOT SET", max_length=20)
    phone_num = models.CharField('Phone Number', max_length=10, default="NOT SET")
    twitter = models.CharField('Twitter', default="NOT SET", max_length=15)
    facebook = models.CharField('Facebook', default="NOT SET", max_length=15)
    line = models.CharField('LINE', default="NOT SET", max_length=10)
    age =  models.CharField('Age', default="NOT SET", max_length=10)
    home_address = models.CharField('Home Address', default="NOT SET", max_length=30)
    home_postalcode = models.CharField('Home Postal Code', default="NOT SET", max_length=10)
    home_province = models.CharField('Home Province', default="NOT SET", max_length=10)
    home_district = models.CharField('Home District', default="NOT SET", max_length=10)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_brief_info(self):
        return self.brief_info

    def get_number(self):
        return self.phone_num

    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)        

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