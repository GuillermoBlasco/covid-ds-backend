from pymongo import MongoClient

client = MongoClient('localhost', 20001)
covid_db = client.covid

def get_country(country_code):
    data = covid_db.country.find({"country_code": country_code})
    for s in data:
        return s
    return None

def get_series_by_code(country_code):
    data = covid_db.series.find({"country_code": country_code})
    return [d for d in data]

