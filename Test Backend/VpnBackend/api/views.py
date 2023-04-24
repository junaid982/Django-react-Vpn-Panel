from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import ApplicationModel , VpnAccountsModel
from django.http import JsonResponse

from .serializers import VpnSerializer


# Create your views here.

@permission_classes((IsAuthenticated,))
@api_view(['POST'])
def allvpn_view(request):

    if request.method == 'POST':

        packagename = request.POST.get('packagename')
        if packagename:
            # get a string data 
            get_country = ApplicationModel.objects.get(packagename = packagename).country
            
            # convert string data into list 
            countries = get_country.split(',')
            
            # fetch all enable vpn accounts related to this countries
            vpnaccounts = VpnAccountsModel.objects.filter(country__in =countries , is_enable = True )
            
            serializer = VpnSerializer(vpnaccounts , many=True)

            return JsonResponse(serializer.data ,safe=False)
    
    return JsonResponse({'Status':'Package Name Not Found'})