import json
import database

def load():
    with open('./data.json') as f:
        data = json.load(f)
        series_data = []
        country_data = []
        for country, d in data.items():
            series = d["data"]
            del d["data"]
            d["country_code"] = country
            country_data.append(d)
            for s in series:
                s["country_code"] = country
                series_data.append(s)
        database.covid_db.country.insert(country_data)
        database.covid_db.series.insert(series_data)