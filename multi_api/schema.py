import graphene
from model_api.schema import Query as BurgerQuery, Mutation as BurgerMutation


class Query(BurgerQuery, graphene.ObjectType):
    pass

class Mutation(BurgerMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
