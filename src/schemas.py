from graphene import (
    ObjectType,
    String,
    Int,
    Boolean,
    List,
    Field,
    Float,
    Mutation,
    InputObjectType,
)
from graphene_mongo import MongoengineObjectType
from geopy.distance import geodesic
from bson import ObjectId
from models.countries import CountryList
from configs import config


class CurrencyType(ObjectType):
    name = String()
    code = String()


class LanguageType(ObjectType):
    name = String()


class CountryListType(MongoengineObjectType):
    class Meta:
        model = CountryList

    name = String()
    independent = Boolean()
    currencies = List(CurrencyType)
    region = String()
    capital = List(String)
    languages = List(LanguageType)
    coordinates = List(Int)
    area = Int()
    population = Int()
    continents = List(String)


class CurrencyInputType(InputObjectType):
    name = String()
    code = String()


class LanguageInputType(InputObjectType):
    name = String()


class CountryListInputType(InputObjectType):
    class Meta:
        model = CountryList

    name = String()
    independent = Boolean()
    currencies = List(CurrencyInputType)
    region = String()
    capital = List(String)
    languages = List(LanguageInputType)
    coordinates = List(Int)
    area = Int()
    population = Int()
    continents = List(String)


class Query(ObjectType):
    countriesQuery = List(
        CountryListType, page=Int(default_value=1), per_page=Int(default_value=10)
    )
    countryQuery = Field(CountryListType, country_id=String(required=True))
    countriesNearbyQuery = List(
        CountryListType, lat=Float(required=True), long=Float(required=True)
    )

    def resolve_countriesQuery(root, info, page, per_page):
        skip = (page - 1) * per_page
        return CountryList.objects.skip(skip).limit(per_page)

    def resolve_countryQuery(root, info, country_id):
        try:
            object_id = ObjectId(country_id)
        except Exception as e:
            raise ValueError("Invalid Country ID")
        country = CountryList.objects.get(id=country_id)
        if country:
            return country
        else:
            raise ValueError("Country not found")

    def resolve_countriesNearbyQuery(root, info, lat, long):
        countries = CountryList.objects.all()
        distances = [
            (country.name, geodesic((lat, long), tuple(country.coordinates)).km)
            for country in countries
        ]
        sorted_distances = sorted(distances, key=lambda x: x[1])[:5]
        nearby_countries = [
            CountryListType(
                name=country,
                independent=False,  # You might need to set this based on your data
            )
            for country, _ in sorted_distances
        ]
        return nearby_countries


class AddCounrtyMutations(Mutation):
    country = Field(lambda: CountryListType)

    class Arguments:
        input_data = CountryListInputType(required=True)

    @staticmethod
    def mutate(root, info, input_data=None):
        new_country = CountryList(**input_data)
        new_country.save()
        return AddCounrtyMutations(country=new_country)


class Mutations(ObjectType):
    addCountryMutation = AddCounrtyMutations.Field()
