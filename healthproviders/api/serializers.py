from rest_framework import serializers
from .models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    #owner = serializers.ReadOnlyField(source='owner.username')
    ProviderName = serializers.CharField(source='name', read_only=True)
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Provider
        fields = ('ProviderName', 'street_address', 'city', 'state',
        'zipcode', 'hospital_referral', 'total_discharges',
        'avg_cov_charges', 'avg_total_payments', 'avg_medicare_payments')
