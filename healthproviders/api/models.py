from django.db import models

# Create your models here.
class Provider(models.Model):
    drg_defintion = models.CharField(max_length=255, blank=False)
    provider_id = models.BigIntegerField(blank=False)
    name  = models.CharField(max_length=255, blank=False)
    street_address = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=False)
    state = models.CharField(max_length=255, blank=False)
    zipcode = models.BigIntegerField(blank=False)
    hospital_referral = models.CharField(max_length=255, blank=False)
    total_discharges = models.BigIntegerField(blank=False)
    avg_cov_charges = models.FloatField(blank=False)
    avg_total_payments = models.FloatField(blank=False)
    avg_medicare_payments = models.FloatField(blank=False)
