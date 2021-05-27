import graphene
from graphene_django import DjangoObjectType

from  .models import Shop, User, Service

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('email', 'username', 'password',  )

class ShopType(DjangoObjectType):
    class Meta:
        model = Shop
        fields = ('shop_name','description', 'image', 'user',)

class ServiceType(DjangoObjectType):
    class Meta:
        model = Service
        fields = ('service',)


class ShopMutation(graphene.Mutation):
    class Arguments:
        shop_name = graphene.String()
        description = graphene.String()
        image = graphene.String()
        is_active = graphene.Boolean()
        user = graphene.ID()

    shop = graphene.Field(ShopType)
    resolved = graphene.Boolean()


    def mutate(self,info, **kwargs):
        id = kwargs['user']
        user = User.objects.get(id=id)
        kwargs['user'] = user
        shop = Shop(**kwargs)
        resolved = True if shop is not None else False
        return ShopMutation(shop=shop, resolved=resolved)

class Mutations(graphene.ObjectType):
    create_shop = ShopMutation.Field()

class Query(graphene.ObjectType):
    
    all_users = graphene.List(UserType)
    all_shops = graphene.List(
                ShopType,
                search = graphene.String(),
                first = graphene.Int(),
                skip = graphene.Int() 
                )

    def resolve_all_users(self, info,  **kwargs):
        qs = User.objects.all()
        return qs
        
    def resolve_all_shops(self, info, search=None, first=None, skip=None):
        qs = Shop.objects.select_related('user').all()
        
        if skip:
            qs = qs[skip:]
        if first:
            qs = qs[:first]
        
        return qs
    

schema = graphene.Schema(query=Query, mutation=Mutations)