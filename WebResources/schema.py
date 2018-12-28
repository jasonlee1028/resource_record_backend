import graphene
from graphene_django import DjangoObjectType

import WebResources.models as model


class ResourceCategory(DjangoObjectType):
    class Meta:
        model = model.ResourceCategory
        interfaces = (graphene.Node,)


class NetResource(DjangoObjectType):
    class Meta:
        model = model.NetResource
        interfaces = (graphene.Node,)


class Query(object):
    resource_category = graphene.List(ResourceCategory,
                                      description="资源分类"
                                      )

    def resolve_resource_category(self, info, **kwargs):
        return model.ResourceCategory.objects.all()

    net_resource = graphene.List(NetResource,
                                 args={
                                     'category_id': graphene.String(required=True,
                                                                    description="资源类型的ID"
                                                                    ),
                                     'start_time': graphene.String(description="开始时间, 格式：YYYY-MM-DD"),
                                     'end_time': graphene.String(description="结束时间, 格式：YYYY-MM-DD"),
                                     'key_word': graphene.String(description="搜索关键字")
                                 },
                                 description="资源列表"
                                 )

    def resolve_net_resource(self, info, **kwargs):
        if kwargs['category_id'] == 'all':
            net_resource_list = model.NetResource.objects.all()
        else:
            _, category_id = graphene.Node.from_global_id(kwargs.get('category_id'))
            print(category_id)
            net_resource_list = model.NetResource.objects.filter(resource_category_id=category_id)

        return net_resource_list

