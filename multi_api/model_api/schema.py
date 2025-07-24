import graphene
import graphql_jwt
from graphene_django.types import DjangoObjectType
from .models import Burger
from graphql_jwt.decorators import login_required
from django import forms

# Serializer ki tarah form
class BurgerForm(forms.ModelForm):
    class Meta:
        model = Burger
        fields = "__all__"

# Type define
class BurgerType(DjangoObjectType):
    class Meta:
        model = Burger

# CRUD Mutations
class CreateBurger(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Int(required=True)
        flavour = graphene.String(required=True)

    burger = graphene.Field(BurgerType)

    @login_required
    def mutate(self, info, name, price, flavour):
        burger = Burger(name=name, price=price, flavour=flavour)
        burger.save()
        return CreateBurger(burger=burger)


class UpdateBurger(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        price = graphene.Int()
        flavour = graphene.String()

    burger = graphene.Field(BurgerType)

    @login_required
    def mutate(self, info, id, name=None, price=None, flavour=None):
        burger = Burger.objects.get(pk=id)
        if name:
            burger.name = name
        if price:
            burger.price = price
        if flavour:
            burger.flavour = flavour
        burger.save()
        return UpdateBurger(burger=burger)


class DeleteBurger(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @login_required
    def mutate(self, info, id):
        burger = Burger.objects.get(pk=id)
        burger.delete()
        return DeleteBurger(ok=True)

# Query aur Mutation root
class Query(graphene.ObjectType):
    all_burgers = graphene.List(BurgerType)

    @login_required
    def resolve_all_burgers(self, info):
        return Burger.objects.all()

class Mutation(graphene.ObjectType):
    create_burger = CreateBurger.Field()
    update_burger = UpdateBurger.Field()
    delete_burger = DeleteBurger.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()     # login
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
