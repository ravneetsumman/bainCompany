from django.test import TestCase, RequestFactory
from django.test.client import Client
from api.models import Provider
from api.views import Providers

class ProviderViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        Provider.objects.create(drg_defintion="test",
                                            provider_id=3453424,
                                            name="Test Health Provider 1",
                                            street_address="2331 Vargas Place",
                                            city="Santa Clara",
                                            state="CA",
                                            zipcode=95050,
                                            hospital_referral="loremispum",
                                            total_discharges="3",
                                            avg_cov_charges="4300",
                                            avg_total_payments="6700",
                                            avg_medicare_payments="1700")
        Provider.objects.create(drg_defintion="test",
                                            provider_id=3453425,
                                            name="Test Health Provider 2",
                                            street_address="2334 Main Street",
                                            city="Atlanta",
                                            state="GA",
                                            zipcode=95050,
                                            hospital_referral="loremispum",
                                            total_discharges="34",
                                            avg_cov_charges="2600",
                                            avg_total_payments="3200",
                                            avg_medicare_payments="2500")

        Provider.objects.create(drg_defintion="test",
                                            provider_id=3453453,
                                            name="Test Health Provider 3",
                                            street_address="2334 Franklin Avenue",
                                            city="Atlanta",
                                            state="GA",
                                            zipcode=95050,
                                            hospital_referral="loremispum",
                                            total_discharges="14",
                                            avg_cov_charges="1440",
                                            avg_total_payments="3200",
                                            avg_medicare_payments="5240")

    def test_all_providers(self):
        # total providers should be 3
        request = self.factory.get('/providers/')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_state_query(self):
        # Georgia should have 2 providers
        request = self.factory.get('/providers/?state=GA')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["ProviderState"], "GA")
        self.assertEqual(response.data[1]["ProviderState"], "GA")

        # California should have 1 provider
        request = self.factory.get('/providers/?state=CA')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["ProviderState"], "CA")

    def test_total_discharges_query(self):
        request = self.factory.get('/providers/?max_discharges=11&min_discharges=1')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["TotalDischarges"], "3")

        request = self.factory.get('/providers/?min_discharges=4&max_discharges=111')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["TotalDischarges"], "34")
        self.assertEqual(response.data[1]["TotalDischarges"], "14")

        request = self.factory.get('/providers/?min_discharges=34&max_discharges=14')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

        request = self.factory.get('/providers/?min_discharges=34&max_discharges=34')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["TotalDischarges"], "34")

    def test_average_covered_charges_query(self):
        request = self.factory.get('/providers/?min_average_covered_charges=4200&max_average_covered_charges=4600')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["AverageCoveredCharges"], "$4300.0")

        request = self.factory.get('/providers/?min_average_covered_charges=400&max_average_covered_charges=3200')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["AverageCoveredCharges"], "$2600.0")
        self.assertEqual(response.data[1]["AverageCoveredCharges"], "$1440.0")

        request = self.factory.get('/providers/?min_average_covered_charges=3400&max_average_covered_charges=1400')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

        request = self.factory.get('/providers/?min_average_covered_charges=2600&max_average_covered_charges=2600')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["AverageCoveredCharges"], "$2600.0")

    def test_average_medicare_payment_query(self):
        request = self.factory.get('/providers/?min_average_medicare_payments=2200&max_average_medicare_payments=2600')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["AverageMedicarePayments"], "$2500.0")

        request = self.factory.get('/providers/?min_average_medicare_payments=400&max_average_medicare_payments=3200')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["AverageMedicarePayments"], "$1700.0")
        self.assertEqual(response.data[1]["AverageMedicarePayments"], "$2500.0")

        request = self.factory.get('/providers/?min_average_medicare_payments=3400&max_average_medicare_payments=1400')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

        request = self.factory.get('/providers/?min_average_medicare_payments=2500&max_average_medicare_payments=2500')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["AverageMedicarePayments"], "$2500.0")

    def test_complex_query(self):
        request = self.factory.get('/providers/?min_average_medicare_payments=2200&max_average_medicare_payments=2600&min_average_covered_charges=2200&max_average_covered_charges=2800')
        response = Providers.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["AverageCoveredCharges"], "$2600.0")
        self.assertEqual(response.data[0]["AverageMedicarePayments"], "$2500.0")
