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


class ResourceStatisticInfo(graphene.ObjectType):
    resource_category_name = graphene.String(description="资源类型名字")
    resource_count = graphene.Int(description="资源类型个数")


class Query(object):
    """
    网络资源查询
    """
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

    resource_statistic = graphene.List(ResourceStatisticInfo, description="资源统计")

    @staticmethod
    def resolve_resource_statistic(root, info, **kwargs):
        resource_statistic_list = list()

        resource_category_objects = model.ResourceCategory.objects.all()
        for resource_category in resource_category_objects:
            count = model.NetResource.objects.filter(resource_category=resource_category).count()
            resource_statistic_list.append(ResourceStatisticInfo(
                resource_category_name=resource_category.display_name,
                resource_count=count
            ))

        return resource_statistic_list


class NewNetResourceData(graphene.InputObjectType):
    """
    新增网络资源的字段
    """
    resource_category_id = graphene.String(required=True, description="资源类型")
    display_name = graphene.String(required=True, description="资源名字")
    url = graphene.String(required=True, description="资源链接")
    description = graphene.String(description="资源描述")


class CreateWebResource(graphene.Mutation):
    """
    新增网络资源
    """
    ok = graphene.Boolean(description="操作状态, 成功(True)或失败(False)")
    error_message = graphene.String(description="错误信息")

    class Arguments:
        new_data = NewNetResourceData(required=True, description="新增资源所包含的所有字段")

    def mutate(self, info, new_data=None):
        ok = True
        error_message = ''

        if not new_data:
            ok = False

        else:
            _, new_data['resource_category_id'] = graphene.Node.from_global_id(new_data['resource_category_id'])
            try:
                model.NetResource.objects.create(**new_data)

            except Exception as e:
                ok = False
                error_message = str(e)

        return CreateWebResource(ok=ok, error_message=error_message)


class Mutation(object):
    """
    操作网络资源
    """
    create_web_resource = CreateWebResource.Field(description="新增网络资源")
