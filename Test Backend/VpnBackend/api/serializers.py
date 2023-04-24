from rest_framework import serializers
from .models import ApplicationModel , VpnAccountsModel



class VpnSerializer(serializers.ModelSerializer):
    class Meta:
        model = VpnAccountsModel
        fields = '__all__'