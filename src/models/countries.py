from mongoengine import (
    Document,
    StringField,
    ListField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    IntField,
    BooleanField,
)


class Currency(EmbeddedDocument):
    code = StringField(required=True)
    name = StringField(required=True)


class Language(EmbeddedDocument):
    name = StringField(required=True)


class CountryList(Document):
    name = StringField(required=True, unique=True)
    independent = BooleanField()
    currencies = ListField(EmbeddedDocumentField(Currency))
    region = StringField()
    capital = ListField(StringField())
    languages = ListField(EmbeddedDocumentField(Language))
    coordinates = ListField(IntField())
    area = IntField()
    population = IntField()
    continents = ListField(StringField())
