# Generated by Django 2.1.4 on 2018-12-28 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebResources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=256)),
                ('url', models.URLField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('resource_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebResources.ResourceCategory')),
            ],
        ),
    ]