from services.fetch_countries import fetch_countries_datas
from services.store_countries_to_db import store_countries_in_db


def task():
    countries = fetch_countries_datas()
    if countries:
        store_countries_in_db(countries)
    else:
        print("Failed to fetch country details from api")


if __name__ == "__main__":
    task()
