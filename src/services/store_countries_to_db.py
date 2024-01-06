from configs import config
from models.countries import CountryList, Currency, Language


def store_countries_in_db(countries):
    try:
        for country in countries:
            languages = [
                Language(name=lang_name)
                for _, lang_name in country.get("languages", {}).items()
            ]
            currencies_data = country.get("currencies", {})
            currencies = [
                Currency(code=currency_code, name=currency_data["name"])
                for currency_code, currency_data in currencies_data.items()
            ]
            country_object = CountryList(
                name=country["name"]["common"],
                independent=country.get("independent", 0),
                currencies=currencies,
                region=country.get("region", ""),
                capital=country.get("capital", []),
                languages=languages,
                coordinates=country.get("latlng", []),
                area=country.get("area", 0),
                population=country.get("population", 0),
                continents=country.get("continents", []),
            )
            country_object.save()
        print("Data written to db successfully")
    except Exception as e:
        print(f"Error occured while saving to db : {e}")
