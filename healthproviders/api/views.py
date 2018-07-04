from django.shortcuts import render
from .models import Provider
from .serializers import ProviderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Providers(APIView):
    """
    List all providers.
    """
    def get(self, request, format=None):
        provider = Provider.objects.all()
        state = self.request.query_params.get('state', None)
        max_discharges = self.request.query_params.get('max_discharges', None)
        min_discharges = self.request.query_params.get('min_discharges', None)
        max_average_covered_charges = self.request.query_params.get('max_average_covered_charges', None)
        min_average_covered_charges = self.request.query_params.get('min_average_covered_charges', None)
        max_average_medicare_payments = self.request.query_params.get('max_average_medicare_payments', None)
        min_average_medicare_payments = self.request.query_params.get('min_average_medicare_payments', None)

        if state is not None:
            provider = provider.filter(state=state)
        if max_discharges is not None:
            provider = provider.filter(total_discharges__lte=max_discharges)#userprofile__level__lte=0
        if min_discharges is not None:
            provider = provider.filter(total_discharges__gte=min_discharges)
        if max_average_covered_charges is not None:
            provider = provider.filter(avg_cov_charges__lte=max_average_covered_charges)
        if min_average_covered_charges is not None:
            provider = provider.filter(avg_cov_charges__gte=min_average_covered_charges)
        if max_average_medicare_payments is not None:
            provider = provider.filter(avg_medicare_payments__lte=max_average_medicare_payments)
        if min_average_medicare_payments is not None:
            provider = provider.filter(avg_medicare_payments__gte=min_average_medicare_payments)

        serializer = ProviderSerializer(provider, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
