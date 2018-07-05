from django.test import TestCase
from api.models import Provider
from api.serializers import  ProviderSerializer

class ProviderSerializerTestCase(TestCase):
    def setUp(self):
        self.provider_attributes = {
            "drg_defintion": "test",
            "provider_id": 3453424,
            "name": "Test Health Provider",
            "street_address": "2337 Vargas Place",
            "city": "Santa Clara",
            "state": "CA",
            "zipcode": "95050",
            "hospital_referral": "loremispum",
            "total_discharges": "34",
            "avg_cov_charges": "$2300",
            "avg_total_payments": "$3200",
            "avg_medicare_payments": "$1500"
        }
        provider = Provider.objects.create(drg_defintion="test",
                                            provider_id=3453424,
                                            name="Test Health Provider",
                                            street_address="2337 Vargas Place",
                                            city="Santa Clara",
                                            state="CA",
                                            zipcode=95050,
                                            hospital_referral="loremispum",
                                            total_discharges="34",
                                            avg_cov_charges="2300",
                                            avg_total_payments="3200",
                                            avg_medicare_payments="1500")
        self.serializer = ProviderSerializer(instance=provider)

    def test_serializer_fields(self):
        data = self.serializer.data
        expected_keys = set(["ProviderName",
                             "ProviderStreetAddress",
                             "ProviderCity",
                             "ProviderState",
                             "ProviderZipCode",
                             "HospitalReferralRegionDescription",
                             "TotalDischarges",
                             "AverageCoveredCharges",
                             "AverageTotalPayment",
                             "AverageMedicarePayments"])
        self.assertEqual(set(data.keys()), expected_keys)

    def test_serializer_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["ProviderName"], self.provider_attributes["name"])
        self.assertEqual(data["ProviderStreetAddress"], self.provider_attributes["street_address"])
        self.assertEqual(data["ProviderCity"], self.provider_attributes["city"])
        self.assertEqual(data["ProviderState"], self.provider_attributes["state"])
        self.assertEqual(data["ProviderZipCode"], self.provider_attributes["zipcode"])
        self.assertEqual(data["HospitalReferralRegionDescription"], self.provider_attributes["hospital_referral"])
        self.assertEqual(data["TotalDischarges"], self.provider_attributes["total_discharges"])
        self.assertEqual(data["AverageCoveredCharges"], self.provider_attributes["avg_cov_charges"])
        self.assertEqual(data["AverageTotalPayment"], self.provider_attributes["avg_total_payments"])
        self.assertEqual(data["AverageMedicarePayments"], self.provider_attributes["avg_medicare_payments"])
