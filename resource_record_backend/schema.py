import graphene
import graphql_jwt

import WebResources.schema


class Query(
    WebResources.schema.Query,
    graphene.ObjectType):
    """
    Graphql Query
    """
    pass


class Mutation(
    WebResources.schema.Mutation,
    graphene.ObjectType):
    """
    Graphql mutation
    """
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
