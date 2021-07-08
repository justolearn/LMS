# Generated by Django 3.2.4 on 2021-07-01 08:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20210701_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='issue_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='customer',
            name='return_date',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
