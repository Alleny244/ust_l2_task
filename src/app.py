from graphene import Schema
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp
from schemas import Query, Mutations

app = FastAPI()
app.add_route(
    "/graphql",
    GraphQLApp(schema=Schema(query=Query, mutation=Mutations)),
    methods=["GET", "POST"],
)
