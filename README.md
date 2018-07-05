# Requirements
Django 2.0.7
mysqlclient 1.3.13
MySQL Data Store

# Project Setup

1) Clone project
2) Activate virtual enviroment using command source env/bin/activate
3) Install MySQL SERVER on system.
4) Run load_data.py in python shell to export csv data into existing database
5) Use this command to server:

    $ `python3 manage.py runserver`
6) Run API http://127.0.0.1:8000/providers, API may take time to load, due to large amount of records.
7) Example query: http://127.0.0.1:8000/providers?max_discharges=28&min_discharges=24&state=GA&min_average_covered_charges=54264.87&max_average_medicare_payments=46853
  Example response:
  ```
  {
      "ProviderName": "EMORY EASTSIDE MEDICAL CENTER",
      "ProviderStreetAddress": "1700 MEDICAL WAY",
      "ProviderCity": "SNELLVILLE",
      "ProviderState": "GA",
      "ProviderZipCode": "30078",
      "HospitalReferralRegionDescription": "GA - Atlanta",
      "TotalDischarges": "26",
      "AverageCoveredCharges": "$62727.23",
      "AverageTotalPayment": "$10747.46",
      "AverageMedicarePayments": "$9843.0"
  },
  {
      "ProviderName": "SOUTH FULTON MEDICAL CENTER",
      "ProviderStreetAddress": "1170 CLEVELAND AVENUE",
      "ProviderCity": "EAST POINT",
      "ProviderState": "GA",
      "ProviderZipCode": "30344",
      "HospitalReferralRegionDescription": "GA - Atlanta",
      "TotalDischarges": "24",
      "AverageCoveredCharges": "$54264.87",
      "AverageTotalPayment": "$5457.58",
      "AverageMedicarePayments": "$4091.04"
  }
  ```
# Tests
  Use this command to run tests:

    $ `python3 manage.py test`
