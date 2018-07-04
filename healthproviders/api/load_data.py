import csv
import os
import sys
from re import sub
from decimal import Decimal

cwd_path =  os.getcwd()
csv_path = cwd_path+'/api/provider.csv'

health_providers_path = cwd_path+'/api/healthproviders/'
sys.path.append(health_providers_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from api.models import Provider
 # Set path of new directory here
#os.chdir(path) # changes the directory
with open(csv_path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Provider()
        p.drg_defintion=row['DRG Definition']
        p.provider_id=row['Provider Id']
        p.name = row['Provider Name']
        p.street_address = row['Provider Street Address']
        p.city = row['Provider City']
        p.state = row['Provider State']
        p.zipcode = row['Provider Zip Code']
        p.hospital_referral = row['Hospital Referral Region Description']
        p.total_discharges = Decimal(sub(r'[^\d.]', '', row[' Total Discharges ']))
        p.avg_cov_charges = Decimal(sub(r'[^\d.]', '', row[' Average Covered Charges ']))
        p.avg_total_payments = Decimal(sub(r'[^\d.]', '', row[' Average Total Payments ']))
        p.avg_medicare_payments = Decimal(sub(r'[^\d.]', '', row['Average Medicare Payments']))
        p.save()

exit()
