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
        "street_address": "1700 MEDICAL WAY",
        "city": "SNELLVILLE",
        "state": "GA",
        "zipcode": 30078,
        "hospital_referral": "GA - Atlanta",
        "total_discharges": 26,
        "avg_cov_charges": 62727.23,
        "avg_total_payments": 10747.46,
        "avg_medicare_payments": 9843
    },
    {
        "ProviderName": "SOUTH FULTON MEDICAL CENTER",
        "street_address": "1170 CLEVELAND AVENUE",
        "city": "EAST POINT",
        "state": "GA",
        "zipcode": 30344,
        "hospital_referral": "GA - Atlanta",
        "total_discharges": 24,
        "avg_cov_charges": 54264.87,
        "avg_total_payments": 5457.58,
        "avg_medicare_payments": 4091.04
    }
    ```
# Tests
  Use this command to run tests:
    $ `python3 manage.py test`
