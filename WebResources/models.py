from django.db import models
from django.utils import timezone

# Create your models here.


class ResourceCategory(models.Model):
    """
    资源种类
    """
    name = models.CharField(max_length=64)
    display_name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.display_name}'


class NetResource(models.Model):
    """
    网络链接资源
    """
    resource_category = models.ForeignKey(ResourceCategory, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=256)
    url = models.URLField(max_length=256)
    description = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'[{self.resource_category.display_name}]:{self.display_name}'


class OriginalCategory(models.Model):
    """
    个人原创资源类型
    """
    name = models.CharField(max_length=64)
    display_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.display_name}'


class OriginalResource(models.Model):
    """
    个人原创资源
    """
    original_category = models.ForeignKey(OriginalCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'

