# Generated by Django 2.2.10 on 2020-02-21 16:41

from django.db import migrations, models
import usaspending_api.common.custom_django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourceassistancetransaction',
            name='created_at',
            field=usaspending_api.common.custom_django_fields.NaiveTimestampField(blank=True, db_index=True, help_text='record creation datetime in Broker', null=True),
        ),
        migrations.AlterField(
            model_name='sourceassistancetransaction',
            name='updated_at',
            field=usaspending_api.common.custom_django_fields.NaiveTimestampField(blank=True, db_index=True, help_text='record last update datetime in Broker', null=True),
        ),
        migrations.AlterField(
            model_name='sourceprocurementtransaction',
            name='created_at',
            field=usaspending_api.common.custom_django_fields.NaiveTimestampField(blank=True, db_index=True, help_text='record creation datetime in Broker', null=True),
        ),
        migrations.AlterField(
            model_name='sourceprocurementtransaction',
            name='updated_at',
            field=usaspending_api.common.custom_django_fields.NaiveTimestampField(blank=True, db_index=True, help_text='record last update datetime in Broker', null=True),
        ),
    ]
