from django.test import TestCase
from api.models import Provider

class ProviderTestCase(TestCase):
    def setUp(self):
        Provider.objects.create(drg_defintion="test", provider_id=3453424,name="ravneet health provider",
        street_address="2337 Vargas Place", city="santa clara",state="CA",zipcode=95050,hospital_referral="loremispum",
        total_discharges=34,
        avg_cov_charges=2300,avg_total_payments=3200,avg_medicare_payments=1500)


    def test_provider_attributes(self):
        response = Provider.objects.get()
        self.assertEqual(response.drg_defintion, "test")
        self.assertEqual(response.provider_id, 3453424)
        self.assertEqual(response.name, "ravneet health provider")
        self.assertEqual(response.street_address, "2337 Vargas Place")
        self.assertEqual(response.city, "santa clara")
        self.assertEqual(response.state, "CA")
        self.assertEqual(response.zipcode, 95050)
        self.assertEqual(response.hospital_referral, "loremispum")
        self.assertEqual(response.total_discharges, 34)
        self.assertEqual(response.avg_cov_charges, 2300)
        self.assertEqual(response.avg_total_payments, 3200)
        self.assertEqual(response.avg_medicare_payments, 1500)
