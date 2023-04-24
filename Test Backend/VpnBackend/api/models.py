from django.db import models

# Create your models here.


class VpnAccountsModel(models.Model):
    privatekey = models.CharField(max_length=150)
    address = models.CharField(max_length=100)
    dns = models.CharField(max_length=100)

    # peers
    publickey = models.CharField(max_length=150)
    presharedkey = models.CharField(max_length=100)
    endpoints = models.CharField(max_length=100)
    allowed_ips = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return self.country + '\t'+self.endpoints
    
class ApplicationModel(models.Model):
    applogo = models.ImageField(upload_to='AppLogo/' ,blank=False)
    appname = models.CharField(max_length=100)
    packagename = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.packagename
    
    