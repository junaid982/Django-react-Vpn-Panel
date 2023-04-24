from django.contrib import admin

from .models import VpnAccountsModel , ApplicationModel

# Register your models here.


# admin.site.register(VpnAccountsModel)

@admin.register(VpnAccountsModel)
class VpnAdmin(admin.ModelAdmin):
    list_display = ['country' ,'created_at' , 'updated_at', 'endpoints' , 'is_enable' , 'privatekey' , 'address' , 'dns' , 'publickey' , 'presharedkey'  , 'allowed_ips' ]


admin.site.register(ApplicationModel)


