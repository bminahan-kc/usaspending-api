# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-05 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0033_add_indexes_to_financial_accounts_by_awards'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummaryTransactionRecipientView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_date', models.DateField()),
                ('fiscal_year', models.IntegerField()),
                ('type', models.TextField()),
                ('pulled_from', models.TextField()),
                ('recipient_hash', models.UUIDField()),
                ('recipient_name', models.TextField()),
                ('recipient_unique_id', models.TextField()),
                ('parent_recipient_unique_id', models.TextField()),
                ('generated_pragmatic_obligation', models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True)),
                ('federal_action_obligation', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('original_loan_subsidy_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True)),
                ('face_value_loan_guarantee', models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True)),
                ('counts', models.IntegerField()),
            ],
            options={
                'db_table': 'summary_transaction_recipient_view',
                'managed': False,
            },
        ),
    ]
