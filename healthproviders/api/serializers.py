from rest_framework import serializers
from .models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    #owner = serializers.ReadOnlyField(source='owner.username')
    ProviderName = serializers.CharField(source='name', read_only=True)
    ProviderStreetAddress = serializers.CharField(source='street_address', read_only=True)
    ProviderCity = serializers.CharField(source='city', read_only=True)
    ProviderState = serializers.CharField(source='state', read_only=True)
    ProviderZipCode = serializers.CharField(source='zipcode', read_only=True)
    HospitalReferralRegionDescription = serializers.CharField(source='hospital_referral', read_only=True)
    TotalDischarges = serializers.CharField(source='total_discharges', read_only=True)
    AverageCoveredCharges = serializers.CharField(source='avg_cov_charges', read_only=True)
    AverageTotalPayment = serializers.CharField(source='avg_total_payments', read_only=True)
    AverageMedicarePayments = serializers.CharField(source='avg_medicare_payments', read_only=True)


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Provider
        fields = ('ProviderName', 'ProviderStreetAddress', 'ProviderCity', 'ProviderState',
        'ProviderZipCode', 'HospitalReferralRegionDescription', 'TotalDischarges',
        'AverageCoveredCharges', 'AverageTotalPayment', 'AverageMedicarePayments')
