import graphene

import WebResources.schema


class Query(
    WebResources.schema.Query,
    graphene.ObjectType):
    """
    Graphql Query
    """
    pass


class Mutation(graphene.ObjectType):
    """
    Graphql mutation
    """
    pass


schema = graphene.Schema(query=Query)
