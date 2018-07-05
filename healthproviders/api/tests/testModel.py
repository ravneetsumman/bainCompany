from django.test import TestCase
from api.models import Provider

class ProviderModelTestCase(TestCase):
    def setUp(self):
        Provider.objects.create(drg_defintion="test",
                                provider_id=3453424,
                                name="Test Health Provider",
                                street_address="2337 Vargas Place",
                                city="Santa Clara",
                                state="CA",
                                zipcode="95050",
                                hospital_referral="loremispum",
                                total_discharges="34",
                                avg_cov_charges=2300,
                                avg_total_payments=3200,
                                avg_medicare_payments=1500)

    def test_provider_attributes(self):
        provider_under_test = Provider.objects.get()
        self.assertEqual(provider_under_test.drg_defintion, "test")
        self.assertEqual(provider_under_test.provider_id, 3453424)
        self.assertEqual(provider_under_test.name, "Test Health Provider")
        self.assertEqual(provider_under_test.street_address, "2337 Vargas Place")
        self.assertEqual(provider_under_test.city, "Santa Clara")
        self.assertEqual(provider_under_test.state, "CA")
        self.assertEqual(provider_under_test.zipcode, 95050)
        self.assertEqual(provider_under_test.hospital_referral, "loremispum")
        self.assertEqual(provider_under_test.total_discharges, 34)
        self.assertEqual(provider_under_test.avg_cov_charges, 2300)
        self.assertEqual(provider_under_test.avg_total_payments, 3200)
        self.assertEqual(provider_under_test.avg_medicare_payments, 1500)
